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


from GeneticAlgorythm import Generation
from datetime import datetime
import gc

print("Started solving at ", datetime.now())
generations = []

generations.append(Generation())

while not generations[len(generations) - 1].validate():
    generations.append(Generation(gen=generations[len(generations) - 1]))
    if len(generations) > 1000:
        del generations[0:len(generations)-5]
        gc.collect()

print("Answer is ", generations[len(generations) - 1].get_ans())
print("Solved at ", datetime.now())
