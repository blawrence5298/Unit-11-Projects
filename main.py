import Project1
import Project2
import Project3

def main():

  projectNum = eval(
  input("Please enter the project number whose output you wish to view: "))
  print("")

  if projectNum == 1:
    age = int(input("Hello! Please enter your age:"))
    Project1.votingAge(age)
    
  elif projectNum == 2:
    three_num = (input("Please list three numbers separated by a comma:"))
    max_list = [int(x) for x in three_num.split(",")]
    max = Project2.maxThree(max_list[0],max_list[1],max_list[2])
    print(max)
    return
  
  elif projectNum == 3:
    Project3.numberGame()
    return
    
  else:
    print("Sorry, that is not a valid project number")
    
main()