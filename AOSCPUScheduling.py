# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:48:37 2019

@author: DEL
"""

import os



def fcfs(self):

	print("First Come First Serve")

	# clear data

	self.turn_around_time['fcfs'] = []

	self.wait_time['fcfs'] = []



	self.turn_around_time['fcfs'].append(self.burst_time[0])

	self.wait_time['fcfs'].append(0) # first process wait time is 0

	if len(self.burst_time) == self.total_process:

		for n in range(1, self.total_process):

			temp = self.burst_time[n-1] + self.wait_time['fcfs'][n-1]

			self.wait_time['fcfs'].append(temp)

			self.turn_around_time['fcfs'].append(temp + self.burst_time[n])



	self.calculate_avg_time('fcfs')

	self.print_data('fcfs')



def sjf(self):

	print("Shortest Job First")

	self.turn_around_time['sjf'] = []

	self.wait_time['sjf'] = []

	# sort using bubble sort

	temp_burst_time = self.burst_time[:]

	for t in range(0, self.total_process):

		for s in range(0, self.total_process-1):

			if temp_burst_time[s] > temp_burst_time[s+1]:

				temp = temp_burst_time[s]

				temp_burst_time[s] = temp_burst_time[s+1]

				temp_burst_time[s+1] = temp



	self.wait_time['sjf'].append(0) # first process wait time is 0

	if len(self.burst_time) == self.total_process:

		for n in range(1, self.total_process):

			temp = self.burst_time[n-1] + self.wait_time['sjf'][n-1]

			self.wait_time['sjf'].append(temp)

			self.turn_around_time['sjf'].append(temp + self.burst_time[n])



	self.calculate_avg_time('sjf')

	self.print_data('sjf')



def ps(self):

	print("Priority Scheduling")

	self.turn_around_time['ps'] = []

	self.wait_time['ps'] = []

	wait = 0

	for t in range(0, max(self.priority)):

		for n in range(0, self.total_process):

			if self.priority[n] == t+1:

				self.wait_time['ps'].append(wait)

				self.turn_around_time['ps'].append(wait + self.burst_time[n])

				wait = wait + self.burst_time[n]



	self.calculate_avg_time('ps')

	self.print_data('ps')



def rr(self):

	print("Round Robin")

	self.turn_around_time['rr'] = []

	self.wait_time['rr'] = []



	remaining_burst_time = self.burst_time[:]

	wt = [0]*self.total_process

	time = 0

	while (1):

		done = True

		for t in range(0, self.total_process):

			if remaining_burst_time[t] > 0:

				done = False

				if remaining_burst_time[t] > self.quantum:

					time += self.quantum

					remaining_burst_time[t] -= self.quantum

				else:

					time += remaining_burst_time[t]

					wt[t] = time - self.burst_time[t]

					remaining_burst_time[t] = 0

		if done == True:

			break



	self.wait_time['rr'] = wt

	self.calculate_avg_time('rr')

	self.print_data('rr')



def wrr(self):

	print("Weighted Round Robin")

	self.turn_around_time['wrr'] = []

	self.wait_time['wrr'] = []



	remaining_burst_time = self.burst_time[:]

	wt = [0]*self.total_process

	time = 0

	while (1):

		done = True

		for t in range(0, self.total_process):

			if remaining_burst_time[t] > 0:

				done = False

				quantum = self.quantum

				if self.weight[t] > 0:

					quantum *= self.weight[t] 

				if remaining_burst_time[t] > quantum:

					time += quantum

					remaining_burst_time[t] -= quantum

				else:

					time += remaining_burst_time[t]

					wt[t] = time - self.burst_time[t]

					remaining_burst_time[t] = 0

		if done == True:

			break



	self.wait_time['wrr'] = wt

	self.calculate_avg_time('wrr')

	self.print_data('wrr')



class cpuschedule:

	total_process = 0

	burst_time = []

	priority = []

	weight = []

	quantum = 0

	wait_time = {

		'fcfs' : [],

		'sjf' : [],

		'ps' : [],

		'rr' : [],

		'wrr' : [],

	}

	total_wait_time = {

		'fcfs' : 0,

		'sjf' : 0,

		'ps' : 0,

		'rr' : 0,

		'wrr' : 0,

	}

	average_wait_time = {

		'fcfs' : 0,

		'sjf' : 0,

		'ps' : 0,

		'rr' : 0,

		'wrr' : 0,

	}

	turn_around_time = {

		'fcfs' : [],

		'sjf' : [],

		'ps' : [],

		'rr' : [],

		'wrr' : [],

	}

	avg_turn_around_time = {

		'fcfs' : 0,

		'sjf' : 0,

		'ps' : 0,

		'rr' : 0,

		'wrr' : 0,

	}



	def getData(self):

		try:



			input_type = input("Use existing data (y/n): ")

			if input_type == 'n':

				self.total_process = int(input("Enter number of processes:"))

				self.burst_time = []

				self.priority = []

				self.weight = []

				for n in range(0, self.total_process):

					bt = input("enter burst time of process "+str(n+1)+": ")

					self.burst_time.append(int(bt))

					p = input("enter priority of process "+str(n+1)+": ")

					self.priority.append(int(p))

					w = input("enter weight of process "+str(n+1)+": ")

					self.weight.append(int(w))

				self.quantum = int(input("enter quantum to use:"))

			elif input_type == 'y':

				self.total_process = 5

				self.burst_time = [8, 4, 10, 20, 2]

				self.priority = [4, 2, 1, 3, 5]

				self.weight = [1, 2, 1, 3, 2]

				self.quantum = 5

			else:

				print("Only y or n. Exiting !!!!")

		except Exception as e:

			print(e)

			print("Sorry input error")



	def calculate_avg_time(self, schedule): # calculate total and average

		for t in range(0, len(self.wait_time[schedule])):

			self.turn_around_time[schedule].append(self.wait_time[schedule][t] + self.burst_time[t])

			self.total_wait_time[schedule] += self.wait_time[schedule][t]



		self.average_wait_time[schedule] = float(self.total_wait_time[schedule])/self.total_process

		self.avg_turn_around_time[schedule] = float(sum(self.turn_around_time[schedule]))/self.total_process



	def print_data(self, schedule):

		print("Total Waiting Time: " + str(self.total_wait_time[schedule]))

		print("Average Waiting Time: " + str(self.average_wait_time[schedule]))

		print("Average Turn Around Time: " + str(self.avg_turn_around_time[schedule]))

		print("\n")



	def write_data(self):

		handle = open("output.txt", 'a')

		path = os.path.abspath("output.txt")

		size = os.path.getsize(path)



		if (size == 0):

			line = "Algorithm".ljust(32)

			line += "Total Waiting Time".ljust(32)

			line += "Average Waiting Time".ljust(32)

			line += "Average Turn Around Time".ljust(32)

			handle.write(line)



		for algo in self.wait_time.keys():

			new_line = algo.ljust(32)

			new_line += str(self.total_wait_time[algo]).ljust(32)

			new_line += str(self.average_wait_time[algo]).ljust(32)

			new_line += str(self.avg_turn_around_time[algo]).ljust(32)

			handle.write(new_line)



		handle.write("\n\n")

		handle.close()



	first_come_first_serve = fcfs

	shortest_job_first = sjf

	priority_schedule = ps

	round_robin = rr

	weighted_round_robin = wrr



schedule = cpuschedule()

try:

	while(1):

		schedule.getData()

		schedule.first_come_first_serve()

		schedule.shortest_job_first()

		schedule.priority_schedule()

		schedule.round_robin()

		schedule.weighted_round_robin()

		schedule.write_data()

		rerun = input("Exit? (y/n): ")

		if rerun == 'y':

			break



except Exception as e:

	print(e)