{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "do I know that variable? 1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def myFunction():\n",
    "    print(\"do I know that variable?\", var)\n",
    "\n",
    "var =1 \n",
    "myFunction()\n",
    "\n",
    "print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"A variable existing outside a function has a scope inside the functions' bodies, excluding those of them which define a variable of the same name.\n",
    "\n",
    "It also means that the scope of a variable existing outside a function is supported only when getting its value (reading). Assigning a value forces the creation of the function's own variable.\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Do I know that variable? 2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "def myFunction():\n",
    "    var = 2\n",
    "    print(\"Do I know that variable?\", var)\n",
    "\n",
    "var = 1\n",
    "myFunction()\n",
    "print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"this name becomes global (it has a global scope, and it doesn't matter whether it's the subject of read or assign).\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Do I know that variable? 2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "def myFunction():\n",
    "    global var\n",
    "    var = 2\n",
    "    print(\"Do I know that variable?\", var)\n",
    "\n",
    "var = 1\n",
    "myFunction()\n",
    "print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "var = 2\n",
    "print(var) #output:2\n",
    "\n",
    "def retVar(): \n",
    "    global var \n",
    "    var = 5\n",
    "    return var\n",
    "\n",
    "print(retVar())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
