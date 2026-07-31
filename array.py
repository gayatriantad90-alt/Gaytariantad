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
        "id": "RkUXWWUcdVM7"
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
        "list=[1,40,4.6,100]\n",
        "print(list)\n",
        "print(list[0:3])\n",
        "print(list[0:4])\n",
        "new_list=[90,1,100,45.4]\n",
        "print(new_list)\n",
        "new_list.append(12)\n",
        "print(new_list)\n",
        "new_list.append(1000)\n",
        "print(new_list[::])\n",
        "new_list.pop(3)\n",
        "print(new_list[::])\n",
        "new_list.insert(2,3)\n",
        "print(new_list[::2])\n",
        "\n",
        "l1=[34,56,4.8,1,0.9]\n",
        "l2=[34,67,9.5,2]\n",
        "print(l1+l2)\n",
        "print(l1+l2+new_list)\n",
        "print(l2+list)\n",
        "\n",
        "fruits = ('apple', 'banana', 'mango', 'date', )\n",
        "sub_tuple = fruits[1:4]\n",
        "print(sub_tuple)\n",
        "\n",
        "data = (10, 20, 30, 40, 50, 60)\n",
        "custom_slice = slice(1, 5, 2)\n",
        "print(data[custom_slice])\n",
        "custom_slice1 = slice(2, 1, 6)\n",
        "print(data[custom_slice1])\n",
        "\n",
        "my_dict = {}\n",
        "my_dict[\"name\"] = \"Gayatri\"\n",
        "my_dict[\"roll no\"] = 5\n",
        "my_dict[\"Department\"] = \"AI&DS\"\n",
        "my_dict[\"Div\"] = 1\n",
        "print(my_dict)\n",
        "\n",
        "\n",
        "num = 79\n",
        "if num > 1:\n",
        "\n",
        "    for i in range(2, num):\n",
        "        if (num % i) == 0:\n",
        "            print(f\"{num} is not a prime number.\")\n",
        "            print(f\"{i} times {num // i} is {num}.\")\n",
        "            break\n",
        "    else:\n",
        "        print(f\"{num} is a prime number.\")\n",
        "else:\n",
        "    print(f\"{num} is not a prime number.\")\n",
        "\n",
        "\n",
        "\n",
        "def year(y):\n",
        "   if year%4==0 :\n",
        "      print(\"leap year:y\")\n",
        "   else:\n",
        "      print(\"no a laep year:y\")\n",
        "y=int(input(\"enter the year\"))"
      ],
      "metadata": {
        "id": "LnBgP7t4dWck",
        "outputId": "2a46df95-0636-4b75-8b32-6488c0373c4a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "====================\n",
            "ARRAY OPERATIONS\n",
            "====================\n",
            "1. 1D Array Operations\n",
            "2. 2D Array Operations\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "1VFDQXmGj92P"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "7CjVzDgBiNSz"
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
        "id": "poMjtDvfdVM8"
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