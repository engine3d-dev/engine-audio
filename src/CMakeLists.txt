
set(AUDIO_INCLUDE_DIRS ../engine-audio)
set(AUDIO_SRC_DIRS engine-audio)

set(
    all_headers
    ${AUDIO_INCLUDE_DIRS}/helper-functions.hpp
    ${AUDIO_INCLUDE_DIRS}/sound.hpp
)

set(
    all_src
    ${AUDIO_SRC_DIRS}/helper-functions.cpp
    ${AUDIO_SRC_DIRS}/sound.cpp
)

add_library(${PROJECT_NAME} ${all_headers} ${all_src}) 
