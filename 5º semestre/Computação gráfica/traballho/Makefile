CXX = g++
CXXFLAGS = -Wall -O2

TARGET = relogio

LIBS = -lGL -lGLU -lglut -lm -lsfml-audio -lsfml-system

SRC = relogio.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(SRC) -o $(TARGET) $(CXXFLAGS) $(LIBS)

clean:
	rm -f $(TARGET)

run: all
	./$(TARGET)
