# © Copyright 2022 Ebrahim Karimi | Gashbeer Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy

from random import randrange


class Generation(object):
    gen = []
    prev_gen = None
    depth = 0

    def cross_over_previous_gen(self):
        self.depth = self.prev_gen.get_gen_depth() + 1
        print("\rGoing to depth ", self.depth, end='')
        for chromosomIndex in range(0, len(self.prev_gen.get_pub())):
            if chromosomIndex % 2 == 0:
                self.gen = self.gen + (
                        self.prev_gen.get_pub()[chromosomIndex] + self.prev_gen.get_pub()[chromosomIndex + 1])

    def init_rand_gen(self):
        self.gen = []
        print("Generating Genesis Generation")
        for xtime in range(0, self.gen_pub_cnt):
            self.gen.append(Chromosome())

    def __init__(self, gen_pub_cnt=200, gen=None):
        if gen is not None:
            self.prev_gen = gen
            self.cross_over_previous_gen()
        else:
            self.gen_pub_cnt = gen_pub_cnt
            self.init_rand_gen()

    def get_gen_depth(self):
        return self.depth

    def validate(self):
        for g in self.gen:
            if g.validate_answer():
                return True
        return False

    def get_ans(self):
        for g in self.gen:
            if g.validate_answer():
                return g
        return None

    def get_pub(self):
        return self.gen


class Chromosome:
    def __init__(self, rows=8, cols=8, arr=None):
        self.queens = list()
        self.rows_cnt = rows
        self.cols_cnt = cols
        if arr is None:
            self.generate_random()
        else:
            self.from_arr(arr)

    def from_arr(self, arr):
        self.arr = arr
        for j in range(0, len(arr)):
            for k in range(0, len(arr[j])):
                if arr[j][k] == 1:
                    self.queens.append((j, k))

    def generate_random(self):
        self.arr = numpy.zeros((self.rows_cnt, self.cols_cnt))
        for i in range(8):
            j = i
            k = randrange(0, self.cols_cnt)
            while (j, k) in self.queens:
                k = randrange(0, self.cols_cnt)
            self.arr[j][k] = 1
            self.queens.append((j, k))

    def validate_xs(self):
        xs = [i[0] for i in self.queens]
        mylist = list(dict.fromkeys(xs))
        return len(mylist) == len(xs)

    def validate_ys(self):
        ys = [i[1] for i in self.queens]
        mylist = list(dict.fromkeys(ys))
        return len(mylist) == len(ys)

    def validate_oblique(self):
        for vert in range(0, len(self.queens)):
            tmp = self.queens
            tmp.remove(self.queens[vert])
            for vertex in tmp:
                x1mx0 = vertex[0] - self.queens[vert][0]
                y1my0 = vertex[1] - self.queens[vert][1]
                if x1mx0 == y1my0:
                    return False
        return True

    def validate_answer(self):
        return self.validate_xs() and self.validate_ys() and self.validate_oblique()

    def __str__(self):
        return "%s\n%s" % (self.arr, self.validate_answer())

    def get_arr(self):
        return self.arr

    def __add__(self, other):
        if not isinstance(other, Chromosome):
            raise ValueError(f'Cannot add chromosome to type {type(other)}')
        c_rnd_1 = randrange(1, 4)
        c_rnd_2 = randrange(4, 7)
        ch1_arr = self.arr
        ch2_arr = other.get_arr()
        for i in range(0, len(self.arr)):
            ch1_arr[i][c_rnd_1:c_rnd_2] = other.get_arr()[i][c_rnd_1:c_rnd_2]
            ch2_arr[i][c_rnd_1:c_rnd_2] = self.arr[i][c_rnd_1:c_rnd_2]
        return [Chromosome(arr=ch1_arr), Chromosome(arr=ch2_arr)]
