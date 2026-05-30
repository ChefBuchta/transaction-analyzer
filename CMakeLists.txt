cmake_minimum_required(VERSION 3.16)

project(TransactionAnalyzer VERSION 1.0 LANGUAGES CXX)

# 3. Striktní vynucení standardu C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
elseif(MSVC)
    add_compile_options(/W4)
endif()

add_executable(Analyzer
    main.cpp
    Account.cpp
    TransactionGraph.cpp
    FraudDetector.cpp
)
