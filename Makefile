# Makefile for quant project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iengine

# Target executable
TARGET = quant

# Source and object files
SRC = engine/main.cpp
OBJ = main.o

# Default rule
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJ)

main.o: $(SRC)
	$(CXX) $(CXXFLAGS) -c $(SRC) -o $(OBJ)

# Clean up build files
clean:
	rm -f $(OBJ) $(TARGET)
