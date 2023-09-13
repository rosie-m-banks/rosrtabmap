#include "custom_msgs/msg/pose3_d.hpp"
#include "custom_msgs/srv/publish_to_rio.hpp"
#include "custom_msgs/srv/get_from_rio.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"
#include "tf2/exceptions.h"
#include "tf2_ros/transform_listener.h"
#include "tf2_ros/buffer.h"
#include <chrono>

#define  _1 std::placeholders::_1

using namespace std;

class NetworkTable : public rclcpp::Node{
    public:
        NetworkTable() : Node("network_table"){

            odometry = this->create_publisher<custom_msgs::msg::Pose3D>("odom", 1);
            accel = this-> create_publisher<custom_msgs::msg::Pose3D>("accel", 1);

            clientA = create_client<custom_msgs::srv::PublishToRio>("publish_to_rio");
            clientB = create_client<custom_msgs::srv::GetFromRio>("get_from_rio");

            tf_buffer_ =
                std::make_unique<tf2_ros::Buffer>(this->get_clock());
            tf_listener_ =
                std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

            timer = this->create_wall_timer(100ms, std::bind(&NetworkTable::update, this));


        }
    private:
        void update(){
            publishRioInfo();
            getRioInfo();
        }
        void publishRioInfo(){
            geometry_msgs::msg::TransformStamped t;
            string toFrameRel = "base_link";
            string fromFrameRel = "map";
            try {
                t = tf_buffer_->lookupTransform(
                    toFrameRel, fromFrameRel,
                    tf2::TimePointZero);
            } catch (const tf2::TransformException & ex) {
                RCLCPP_INFO(
                    this->get_logger(), "Could not transform %s to %s: %s",
                    toFrameRel.c_str(), fromFrameRel.c_str(), ex.what());
                return;
            }


            auto req = std::make_shared<custom_msgs::srv::PublishToRio::Request>();
            req->a = t.transform;
            auto future = clientA->async_send_request(req);

            auto result = future.get();
        }
        void getRioInfo(){
            auto request = std::make_shared<custom_msgs::srv::GetFromRio::Request>();
            request -> a = true;
            auto future = clientB->async_send_request(request);

            auto result = future.get();
            auto message = result->b;
            auto acceler = result->c;
            odometry->publish(message);
            accel->publish(acceler);

            
        }

    rclcpp::Publisher<custom_msgs::msg::Pose3D>::SharedPtr odometry;
    rclcpp::Publisher<custom_msgs::msg::Pose3D>::SharedPtr accel;

    rclcpp::Client<custom_msgs::srv::PublishToRio>::SharedPtr clientA;
    rclcpp::Client<custom_msgs::srv::GetFromRio>::SharedPtr clientB;

    rclcpp::TimerBase::SharedPtr timer;

    std::shared_ptr<tf2_ros::TransformListener> tf_listener_{nullptr};
    std::unique_ptr<tf2_ros::Buffer> tf_buffer_;
   
}; 


int main(int argc, char * argv[]){

    rclcpp::init(argc, argv);
    rclcpp::spin(make_shared<NetworkTable>());
    rclcpp::shutdown();

    return 0;
}

