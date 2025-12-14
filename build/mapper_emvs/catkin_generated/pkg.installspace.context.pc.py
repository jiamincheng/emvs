# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;sensor_msgs;dvs_msgs;camera_info_manager;image_geometry;minkindr;cartesian3dgrid;rosbag;glog_catkin;gflags_catkin;pcl_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lmapper_emvs".split(';') if "-lmapper_emvs" != "" else []
PROJECT_NAME = "mapper_emvs"
PROJECT_SPACE_DIR = "/home/jiamin/emvs_ws/install"
PROJECT_VERSION = "0.0.0"
