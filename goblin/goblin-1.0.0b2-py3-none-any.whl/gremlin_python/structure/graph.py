'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

__author__ = 'Marko A. Rodriguez (http://markorodriguez.com)'

from gremlin_python.process.graph_traversal import GraphTraversalSource
from gremlin_python.process.traversal import TraversalStrategies


class Graph(object):
    def __init__(self):
        if self.__class__ not in TraversalStrategies.global_cache:
            TraversalStrategies.global_cache[self.__class__] = TraversalStrategies()

    def traversal(self):
        return GraphTraversalSource(self, TraversalStrategies.global_cache[self.__class__])

    def __repr__(self):
        return "graph[empty]"


class Element(object):
    def __init__(self, id, label):
        self.id = id
        self.label = label

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Vertex(Element):
    def __init__(self, id, label="vertex"):
        Element.__init__(self, id, label)

    def __repr__(self):
        return "v[" + str(self.id) + "]"


class Edge(Element):
    def __init__(self, id, outV, label, inV):
        Element.__init__(self, id, label)
        self.outV = outV
        self.inV = inV

    def __repr__(self):
        return "e[" + str(self.id) + "][" + str(self.outV.id) + "-" + self.label + "->" + str(self.inV.id) + "]"


class VertexProperty(Element):
    def __init__(self, id, label, value):
        Element.__init__(self, id, label)
        self.value = value
        self.key = self.label

    def __repr__(self):
        return "vp[" + str(self.label) + "->" + str(self.value)[0:20] + "]"


class Property(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "p[" + str(self.key) + "->" + str(self.value)[0:20] + "]"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.key == other.key and self.value == other.value

    def __hash__(self):
        return hash(self.key) + hash(self.value)
