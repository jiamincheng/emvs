execute_process(COMMAND "/home/jiamin/emvs_ws/build/dvs_simulator_py/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jiamin/emvs_ws/build/dvs_simulator_py/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
