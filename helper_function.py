import geocoder
import geopy
import numpy as np
import geopy.distance
from geopy.geocoders import Nominatim

#get locaiton of the user directly
def choose1():
    ip = geocoder.ip('me')
    user_loc=ip.latlng
    user_loc=(user_loc[1], user_loc[0])
    return user_loc

#get distance between 2 latitude longitude coordinates
def distance(loc1, loc2):
    ans= geopy.distance.geodesic(loc1, loc2).km
    return ans

#find the closest node from a certain location
def nearest_node(userloc, G):
    em=[]
    for i in G:
        coords_1 = (userloc[0], userloc[1]) #coordinats of user
        value = G[i]
        lng_h, lat_h = value[0], value[1]
        coords_2 = (lng_h, lat_h)            #coordinates of hospital
        ans = geopy.distance.geodesic(coords_2, coords_1).km
        em.append([i, ans])
    least=''
    value=999999999999
    for i in em:       #i = [hospital name, distance]
        if i[1]<value:
            least = i[0]
            value = i[1]
    return least, value

def enQueue(lst,a):
  lst.append(a)
  return lst

def deQueue(lst):
  a = lst.pop(0)
  return a

def dijkstra(graph, source):
  dj = {}   #dictionary to set node distance to infinity and later update it
  dj[source] = [source,0]
  for node in graph:
    if node!= source:
      dj[node] = ['-', 999999999]  #set each node's distance to infinity
    
  visited = []
  while len(dj)!= len(visited):
    min_dist = 999999999
    for node in dj:
      if node not in visited and dj[node][1]< min_dist:
        min_node = node
        min_dist = dj[node][1]
    visited.append(min_node)
    for neighbor in graph[min_node]:
      distance = dj[min_node][1] + neighbor[1]
      if dj[neighbor[0]][1]> distance:
        dj[neighbor[0]][1] = distance
        dj[neighbor[0]][0] = min_node
  return dj

def getShortestPath(graph, source, to):
  dist = dijkstra(graph, source)
  em = [to]
  key=''
  final = to
  while em[-1][0]!= source:
    find = to
    for i in dist:
      if i==find:
        key = dist[i][0]
        ans = (key, find)
        em.append(ans)
        to = key
        break
  em.pop(0)
  distance_shortest = dist[final][1]
  print('the nearest hospital is', distance_shortest, 'km away.')
  return em[::-1] 