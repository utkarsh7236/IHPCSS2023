CC = gfortran
CFLAGS += -O3 -fopenmp
SRC_DIR=src
BIN_DIR=bin

default: all

all: create_directory \
	 $(BIN_DIR)/loops

create_directory:
	@mkdir -p $(BIN_DIR)

$(BIN_DIR)/loops: $(SRC_DIR)/loops.f08
	$(CC) -o $@ $< $(CFLAGS)
