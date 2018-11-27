#!/usr/bin/env python3

"""currency.py: Inquiring exchange rate..

__author__ = "Xiaxinyi"
__pkuid__  = "1700017788"
__email__  = "1700017788@pku.edu.cn"
__last-edited__="2018/11/27"
"""
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

from urllib.request import urlopen

def exchange(currencyfrom,currencyto,amount):
    """
    calculate currency amount
    :param currencyfrom: the currency you own now
    :param currencyto: the currency you want to exchange into
    :param amount: the amount of your current currency
    :return: the amount of your object currency you will get
    """
    web="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+currencyfrom.upper()+"&to="+currencyto.upper()+"&amt="+amount
    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    # change into correct format
    jstr=jstr.replace("true","True")
    jstr=jstr.replace("false","False")
    # generate a dictionary
    currencydict=dict(eval(jstr))
    # validity checking
    if currencydict['success'] == False:
        print('invalid format')
    else:
        firstversion=currencydict["to"].strip('"')
        ans=firstversion[:firstversion.find(" ")]
        ans=round(float(ans),5)
        return ans

######################################################

def test_exchange(cuf,cut,cuamt,curst):
    """
    test function
    :param cuf: currencyfrom to check
    :param cut:  currencyto to check
    :param cuamt: amount of currencyfrom to check
    :param curst: amount of currencyto you will get
    :return:
    """
    assert (curst==exchange(cuf,cut,cuamt,curst))

def testAll():
    """
    put the amount into test function
    :return: Assertion error if not passed
    """
    test1=["USD","EUR","10",8.63569]
    test2=["irr","jmd","20",0.06376]
    test3=["HRK","JPY","5",86.80235]
    test4=["LAK","LBP","3",0.53268]
    test5=["usd","CNY","1",6.8521]
    test=[test1,test2,test3,test4,test5]
    for testi in test:
        test_exchange(testi[0],testi[1],testi[2],testi[3])
    print('test passed')
    
###########################################################

def main():
    """
    main function
    :return: the result
    """
    testAll()
    currencyfrom = input("Please input your currency on hand:")
    currencyto = input("Please input the currency you want to convert to:")
    amount = input("Please input the amount of your current on hand:")
    print(exchange(currencyfrom, currencyto, amount))

if __name__ == '__main__':
    main()
