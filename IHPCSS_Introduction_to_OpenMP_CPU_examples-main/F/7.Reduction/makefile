CC = gfortran
CFLAGS += -O3 -fopenmp
SRC_DIR=src
BIN_DIR=bin

default: all

all: create_directory \
	 $(BIN_DIR)/reduction

create_directory:
	@mkdir -p $(BIN_DIR)

$(BIN_DIR)/reduction: $(SRC_DIR)/reduction.f08
	$(CC) -o $@ $< $(CFLAGS)
