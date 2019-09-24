cmake_minimum_required(VERSION 2.8.9)
project (TestLibrary)

set(PROJECT_LINK_LIBS libMyEngineDynamic.so)
link_directories(../build)

include_directories(../myengine)
add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic ${PROJECT_LINK_LIBS})

set(PROJECT_LINK_LIBS libMyEngineStatic.a)
link_directories(../build)

include_directories(../myengine)
add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic ${PROJECT_LINK_LIBS})
