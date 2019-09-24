cmake_minimum_required(VERSION 2.8)
project(hello)
add_executable(hello helloworld.cpp)

find_package(Threads)
add_executable(usespthread usespthread.cpp)
target_link_libraries(usespthread ${CMAKE_THREAD_LIBS_INIT})

set(CMAKE_BUILD_TYPE Release)
include_directories(myengine)

file(GLOB SOURCES "myengine/*.cpp")

add_library(MyEngineDynamic SHARED ${SOURCES})
set_target_properties(MyEngineDynamic PROPERTIES PUBLIC_HEADER "myengine/myengine.hpp")
install(TARGETS MyEngineDynamic 
		LIBRARY DESTINATION /usr/local/lib
		PUBLIC_HEADER DESTINATION /usr/local/include)

add_library(MyEngineStatic STATIC ${SOURCES})
set_target_properties(MyEngineStatic PROPERTIES PUBLIC_HEADER "myengine/myengine.hpp")
install(TARGETS MyEngineStatic 
		ARCHIVE DESTINATION /usr/local/lib
		LIBRARY DESTINATION /usr/local/lib
		PUBLIC_HEADER DESTINATION /usr/local/include)

