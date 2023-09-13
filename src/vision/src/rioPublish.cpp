#include "rclcpp/rclcpp.hpp"
#include "custom_msgs/srv/publish_to_rio.hpp"
#include "geometry_msgs/msg/transform.hpp"
#include "ntcore_cpp.h"

using namespace std;
class publish{

    NT_Publisher pub;

    public:
        explicit publish(NT_Topic topic){
            pub = nt::Publish(topic, NT_DOUBLE_ARRAY, "double_array");
        }

        void sendInfo(const std::shared_ptr<custom_msgs::srv::PublishToRio::Request> req){
            auto translation = req->a.translation;
            double pose[7] = {req->a.translation.x, req->a.translation.y, req->a.translation.z, 
            req->a.rotation.w, req->a.rotation.x, req->a.rotation.y, req->a.rotation.z};
            nt::SetDoubleArray(pub, pose);
        }
        ~publish() {
            nt::Unpublish(pub);
        }


};


void publishPose(const std::shared_ptr<custom_msgs::srv::PublishToRio::Request> request,
          std::shared_ptr<custom_msgs::srv::PublishToRio::Response>      response){
    publish sendToRio(nt::GetTopic(nt::GetDefaultInstance(), "pose"));
    sendToRio.sendInfo(request);
    response->b = true;
}


int main(int argc, char **argv){
    

    rclcpp::init(argc, argv);

    shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("publish_to_rio");

    rclcpp::Service<custom_msgs::srv::PublishToRio>::SharedPtr service = 
    node->create_service<custom_msgs::srv::PublishToRio>("publish_to_rio", &publishPose);

    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}