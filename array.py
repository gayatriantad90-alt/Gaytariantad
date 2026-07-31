{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gayatriantad90-alt/Gaytariantad/blob/main/array.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ms_X4R9Gnun0"
      },
      "source": [
        "# Lecture live chat\n",
        "\n",
        "To allow anonymous chat, response and polling, I'm going to try the jit.si chatroom here:\n",
        "\n",
        "https://meet.jit.si/CCP5PythonPit\n",
        "\n",
        "Join if you want to respond to the polls, or anonymously ask questions (choose a funny username if you go anonymous). You can ignore the camera/microphone permission if you like. Alternatively, you can of course just talk in the class, although my experience shows this is rare in large classes."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class OneDarray:\n",
        "  def_init_(self,initial_size=10):\n",
        "    \"\"\"Initalize 1D array with given size \"\"\"\n",
        "    self.size=inital_size\n",
        "    self.array=[none]*self.size\n",
        "\n",
        "    def display(self):\n",
        "        \"\"\"Display the current array elements\"\"\"\n",
        "        if self.length == 0:\n",
        "            print(\"Array is empty\")\n",
        "            return\n",
        "        print(\"Current Array:\", end=\" \")\n",
        "        for i in range(self.length):\n",
        "            print(self.array[i], end=\" \")\n",
        "        print()\n",
        "        print(f\"Size: {self.size}, Length: {self.length}\")\n",
        "\n",
        "    def insert_at_end(self, value):\n",
        "        \"\"\"Insert element at the end of array\"\"\"\n",
        "        if self.length >= self.size:\n",
        "            print(\"Array is full! Cannot insert\")\n",
        "            return False\n",
        "\n",
        "        self.array[self.length] = value\n",
        "        self.length += 1\n",
        "        print(f\"Inserted {value} at end\")\n",
        "        return True\n",
        "\n",
        "    def insert_at_position(self, position, value):\n",
        "        \"\"\"Insert element at specific position (0-based index)\"\"\"\n",
        "        if position < 0 or position > self.length:\n",
        "            print(f\"Invalid position! Must be between 0 and {self.length}\")\n",
        "            return False\n",
        "\n",
        "        if self.length >= self.size:\n",
        "            print(\"Array is full! Cannot insert\")\n",
        "            return False\n",
        "\n",
        "\n",
        "        for i in range(self.length, position, -1):\n",
        "            self.array[i] = self.array[i - 1]\n",
        "\n",
        "        self.array[position] = value\n",
        "        self.length += 1\n",
        "        print(f\"Inserted {value} at position {position}\")\n",
        "        return True\n",
        "\n",
        "    def delete_at_end(self):\n",
        "        \"\"\"Delete element from the end\"\"\"\n",
        "        if self.length == 0:\n",
        "            print(\"Array is empty! Cannot delete\")\n",
        "            return None\n",
        "\n",
        "        deleted_value = self.array[self.length - 1]\n",
        "        self.array[self.length - 1] = None\n",
        "        self.length -= 1\n",
        "        print(f\"Deleted {deleted_value} from end\")\n",
        "        return deleted_value\n",
        "\n",
        "    def delect_at_position(self,postion):\n",
        "      \"\"\"delete element at the spesific position (0-based index)\"\"\"\n",
        "      if self.length==0:\n",
        "        print(f\"array is emppty! Cannot delect\")\n",
        "        return None\n",
        "\n",
        "        if  position<0 or position >=self.length:\n",
        "          print(f\"Invalid postion! Must be between 0 and {self. length-1}\")\n",
        "          delected_value=self.array[position]\n",
        "          for i in range(positin,self.length-1):\n",
        "            self.array[i+1]\n",
        "            self.array[self.length-1]=None\n",
        "            self.length-= 1\n",
        "        print(f\"Deleted {deleted_value} from position {position}\")\n",
        "        return deleted_value\n",
        "\n",
        "    def search(self, value):\n",
        "        \"\"\"Search for an element in the array\"\"\"\n",
        "        for i in range(self.length):\n",
        "            if self.array[i] == value:\n",
        "                print(f\"Found {value} at position {i}\")\n",
        "                return i\n",
        "        print(f\"Value {value} not found in array\")\n",
        "        return -1\n",
        "\n",
        "    def search_all_occurrences(self, value):\n",
        "        \"\"\"Search for all occurrences of an element\"\"\"\n",
        "        positions = []\n",
        "        for i in range(self.length):\n",
        "            if self.array[i] == value:\n",
        "                positions.append(i)\n",
        "\n",
        "        if positions:\n",
        "            print(f\"Found {value} at positions: {positions}\")\n",
        "            return positions\n",
        "        else:\n",
        "            print(f\"Value {value} not found in array\")\n",
        "            return []\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ElraJvYsnv33"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "ULsppl_fzeZ_"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "FDP2Wd0TyKoI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rTTdYpnazP68"
      },
      "source": [
        "# Tutorial contents\n",
        "\n",
        "Every programming tutorial is like this:\n",
        "![How to draw an owl. Draw two circles. Then draw the rest of the owl.](https://github.com/toastedcrumpets/CCP5_Python_examples/blob/master/owlanomics.png?raw=1)\n",
        "\n",
        "This is no different, it is the nature of the problem. Learning programming is exactly like playing music, the good and the bad.\n",
        "As you start to learn music/code, your music/code will not work at first, then it will sound/run terrible, but you must practice and learn to \"fail upwards\" by learning what \"sounds\"/runs nice.\n",
        "\n",
        "A massive aspect is learning how you fail, coding is 1/3rds programming, then 2/3rds finding the errors/unconsidered-complications. Good programmers still make many mistakes, they just write code so the mistakes are obvious and easy to find.\n",
        "\n",
        "Eventually you will become a maestro with practice, and will be able to improv code that makes your non-programmer friends stare in amazement. Fair warning though, music might help you make more friends, but programming will make computers do your work for you so you have more time for the finer aspects of life.\n",
        "\n",
        "I cannot hope to teach you everything about programming in two-days, so I hope to show you a quick overview, teach you very carefully the hardest part of python (the reference/side-affects/spooky action at a distance). Finally, we'll talk about examples, as you'll probably eventually learn programming from googling your problem and reading other peoples code.\n",
        "\n",
        "<br/>\n",
        "<center><b>Please give me suggestions of interesting things to code! I will code them for you as an example.</b></center>\n",
        "\n",
        "Everything in here is code/an-example, you can edit these pages, change them, rerun the code. You must do this, break it, learn how to understand your errors, then learn how to put it back together in interesting ways.\n",
        "\n",
        "## Drawing two circles\n",
        "* [Installing python](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/00-Installing_python.ipynb)\n",
        "* [Introduction to python](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/01-Introduction.ipynb)\n",
        "* [Variable scope (and calculating prime numbers)](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/02-Variable%20scope%20(calclulating%20prime%20numbers).ipynb)\n",
        "* [Calculating $\\pi$](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/03-Calculating%20pi.ipynb)\n",
        "* [Handling errors (AKA Fantastic Exceptions and where to find them)](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/04-Errors%20(Fantastic%20Exceptions%20and%20where%20to%20find%20them).ipynb)\n",
        "* [List comprehensions, lambdas, and running other programs](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/07-List%20comprehensions%2C%20lambdas%2C%20and%20running%20other%20programs.ipynb)\n",
        "\n",
        "## The rest of python\n",
        "\n",
        "* [Example: Stock/Data analysis using Pandas](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/05-%20Example%2C%20Stock%20analysis%20using%20pandas.ipynb)\n",
        "* [Example: Molecular dynamics in python](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/06-%20Example%2C%20Molecular%20dynamics%20simulations.ipynb)\n",
        "* [Appendix: Snippets of python code (request anything you like!)](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/Appendix-A-Snippets.ipynb)\n",
        "* [Appendix: Monte Carlo calculation of PI with animation](https://colab.research.google.com/github/toastedcrumpets/CCP5_Python_examples/blob/master/Appendix-B-%20Monte%20Carlo%20class%20examples.ipynb)\n",
        "* [Dall-E notebooks for image generation](https://alpha2phi.medium.com/generate-image-from-text-c84daaddd75b)\n",
        "* [Music generation from facebook](https://huggingface.co/spaces/facebook/MusicGen) (see the repo for the collab links)\n",
        "\n",
        "## For more examples, ask me to program something you need!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z29dLCU6nun1"
      },
      "source": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Table of contents for collab.research.google.com.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
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
      "version": "3.10.6"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}