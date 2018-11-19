from Skilaverkefni_6.py import Skraning
from mysql.connector import Error

try:
    test = Skraning()
    test.nyr_medlimur("Axel Máni")
    test.nyr_afangi("Axel Máni")
    test.prenta("Axel Máni")
    test.prenta("Axel Máni")
    test.skraning("Axel Máni")
    test.prenta("Axel Máni")
    test.skradurIafanga("Axel Máni")
except Error as e:
    print("villa",e)
