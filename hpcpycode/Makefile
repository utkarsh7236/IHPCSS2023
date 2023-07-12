# Makefile for the compiled version for comparison with parallel python codes
# Ramses van Zon
# SciNetHPC, 2017-2019

TIME=time -p
CXXFLAGS=-O3 -march=native
FFLAGS=-O3 -march=native
LDLIBS=-lcpgplot -lpgplot -lX11 -lxcb -ldl -lXau -lgfortran -lpng
CC=gcc
CXX=g++
F90=gfortran



all: auc_serial_cpp.ex auc_serial_f90.ex diff2d_cpp.ex diff2d_f90.ex diff2dplot_f90.mod

run: run_diff2d_cpp run_diff2d_f90 run_auc_serial_cpp



.PHONY: all clean run_diff2d_cpp run_diff2d_f90 distclean

run_auc_serial_cpp: auc_serial_cpp.ex
	$(TIME) ./$< 

run_diff2d_cpp: diff2d_cpp.ex
	$(TIME) ./$< 

run_diff2d_f90: diff2d_f90.ex
	$(TIME) ./$< 

auc_serial_cpp.o: auc_serial.cpp
	$(CXX) -c $(CXXFLAGS) -o $@ $<

auc_serial_f90.o: auc_serial.f90
	$(F90) -c $(FFLAGS) -o $@ $<

diff2d_cpp.o: diff2d.cpp diff2dparams.py diff2dplot.h
	$(CXX) -c $(CXXFLAGS) -o $@ $<

diff2d_f90.o: diff2d.f90 diff2dparams.py diff2dplot_f90.o
	$(F90) -c $(FFLAGS) -o $@ $<

diff2dplot_f90.mod: diff2dplot_f90.o
diff2dplot_f90.o: diff2dplot.f90 pgplot90.mod
	$(F90) -c $(FFLAGS) -o $@ $<

pgplot90.mod: pgplot90.o
pgplot90.o: pgplot90.f90
	$(F90) -c $(FFLAGS) -o $@ $<

diff2dplot_cpp.o: diff2dplot.cpp
	$(CXX) -c $(CXXFLAGS) -o $@ $<

auc_serial_cpp.ex : auc_serial.o
	$(CXX) $(LDFLAGS) -o $@ $^ 

auc_serial_f90.ex : auc_serial_f90.o
	$(F90) $(LDFLAGS) -o $@ $^ $(LDLIBS)

diff2d_cpp.ex : diff2d_cpp.o diff2dplot_cpp.o
	$(CXX) $(LDFLAGS) -o $@ $^ $(LDLIBS)

diff2d_f90.ex : diff2d_f90.o diff2dplot_f90.o pgplot90.o
	$(F90) $(LDFLAGS) -o $@ $^ $(LDLIBS)

clean:
	$(RM) *.o *.ex *.mod

distclean: clean
	$(RM) output_*.txt *.lprof *.out
	$(RM) -r __pycache__ 
