#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import rospy
import std_msgs.msg
import time
import math
import numpy as np
import tf, tf2_ros
import json
import copy
import random
import rospkg
import yaml
import io
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from xml.dom import minidom
from gazebo_msgs.srv import DeleteModel,SpawnModel
from visualization_msgs.msg import Marker
from jsk_recognition_msgs.msg import BoundingBox, BoundingBoxArray, TorusArray, PolygonArray
from jsk_recognition_msgs.msg import Torus as jsk_Torus
from sympy import Point3D, Line3D, Segment3D
from sympy import Point as Point2D
from sympy import Polygon as Polygon2D
import xml.etree.ElementTree

v1 =  [0.0002110004425048828,
 0.0003459453582763672,
 0.0003020763397216797,
 0.00022411346435546875,
 0.00026297569274902344,
 0.00018405914306640625,
 0.0003838539123535156,
 0.0004620552062988281,
 0.0001819133758544922,
 0.00031113624572753906,
 0.0012428760528564453,
 0.00022101402282714844,
 0.0005009174346923828,
 0.00023412704467773438,
 0.0001480579376220703,
 0.00022912025451660156]

v2 = [ 0.0003199577331542969,
 0.0009760856628417969,
 0.0003311634063720703,
 0.00023794174194335938,
 0.0002751350402832031,
 0.000308990478515625,
 0.00031495094299316406,
 0.00028514862060546875,
 0.00047016143798828125,
 0.0002739429473876953,
 0.00020194053649902344,
 0.00023818016052246094,
 0.00028514862060546875,
 0.0002810955047607422,
 0.0002951622009277344]

v3 = [ 0.0002689361572265625,
 0.00028705596923828125,
 0.0006558895111083984,
 0.0007169246673583984,
 0.00033593177795410156,
 0.0003380775451660156,
 0.00028705596923828125,
 0.00043892860412597656,
 0.00024199485778808594,
 0.0004990100860595703,
 0.0002620220184326172,
 0.00044798851013183594,
 0.000247955322265625]

print(np.mean(v1),np.mean(v2),np.mean(v3))
