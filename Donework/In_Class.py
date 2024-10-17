# class Cat:
#   def __init__(self,name,breed,age):
#     self.name=name
#     self.breed=breed
#     self.age=age

#   def meow(self):
#     print("meeeeeuuuuwwww")
# my_cat=Cat("Minky","British Shorthair",2)
# print(my_cat.name)
# print(my_cat.breed)
# print(my_cat.age)
# my_cat.meow()


# class car():
#   def __init__(self,name):
#     self.name=name
#   def speak(self):
#     print("I am an automobile.")

# class maruti(car):
#   def honk(self):
#     print("bhum bhum")
# car_mine=maruti("maruti800")

# print(car_mine.name)
    


# class Animal:
#   def __init__(self,name):
#     self.name=name
#   def speak(self):
#     pass
# class horse(Animal):
#   def speak(self):
#     return f"{self.name} says neighhhhhhhh!"

# class elephant(Animal):
#   def speak(self):
#     return f"{self.name} says trumpettttt!"


# horse=horse("Buddy")
# elephant=elephant("Dumble")


# print(horse.speak())
# print(elephant.speak())


# car_mine.speak()
# car_mine.honk()












data_students={}

def adding():
  name=input("Enter student name ")
  age=int(input("Enter student age "))
  grade=input("Enter student grade ")
  id=len(data_students)+1
  data_students[id]={
    'name':name,
    'age':age,
    'grade':grade
  }
  print(f"Student {name} added with ID: {id}")

def details(id):
  student=data_students.get(id)
  if student:
    print(f"Student ID: {id}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
  else:
    print("Student Not Found")

def delectinginfo(id):
  if id in data_students:
    del data_students[id]
    print(f"Student with ID {id} removed")
  else:
    print("Student not Found")

def main():
  while True:
    print("\nStudent Management System")
    print("1: Add Students")
    print("2: Display Student Details")
    print("3: Display all Students")
    print("4: Remove Students")
    print("5: Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
      adding()
    elif(choice==2):
      student_id=int(input("Enter Student ID "))
      details(student_id)
    elif(choice==3):
      showalldata()
    elif(choice==4):
      student_id=int(input("Enter Student ID "))
      delectinginfo(student_id)
    elif(choice==5):
      print("Exiting the program")
      break
    else:
      print("Invalid choice.please try again.")
main()

def showalldata():
  print("Studentlist:")
  for id, student in data_students.items():
    print(f"ID:{id},Name:{student['name']}")
      

















# def drawboard(board):
#   for row in board:
#     print("|".join(row))
#     print("-"*9)




# def winner(board,player):
#   for i in range(3):
#     if all(board[i][j]==player for j in range(3) or all (board[j][i] ==player for j in range(3))):
#       return True
#   if all(board[i][j]==player for i in range(3) or all(board[i][2-i]==player for i in range(3))):
#     return True
#   return False



# def boardfull(board):
#   return all(board[i][j]!=''for i in range(3) for j in range(3))

# board=[[''for _ in range(3)]for _ in range(3)]
# drawboard(board)


# def drawboardindex(board):
#   line="------------"
#   print(" 0   1    2")
#   for i,row in enumerate(board):
#     print(i,end=" ")
#     for cell in row:
#       print(f"| {cell}",end="")
#     print("|")
#     print(line)
    
  














# import pygame,sys
# from pygame.locals import QUIT

# pygame.init()

# window_width,window_height=400,300
# window=pygame.display.set_mode((window_width,window_height))
# pygame.display.set_caption("Ping Pong")
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# WHITE = (255, 255, 255)


# paddle_width, paddle_height = 80, 10
# paddle_x, paddle_y = (window_width - paddle_width) // 2, window_height - paddle_height - 10

# ball_radius=5
# ball_x,ball_y=window_width//2,window_height//2
# ball_speed_x,ball_speed_y=3,-3
# Score=0
# font=pygame.font.Font(None,36)
# game_over=False
# while not game_over:
#   for event in pygame.event.get():
#     if event.type==QUIT:
#       pygame.quit()
#       sys.exit()
#   keys=pygame.key.get_pressed()
#   if keys[pygame.K_LEFT] and paddle_x>0:
#     paddle_x-=5
#   if keys[pygame.K_RIGHT] and paddle_x<window_width-paddle_width:
#     paddle_x+=5

#   ball_x+=ball_speed_x
#   ball_y+=ball_speed_y

#   window.fill(WHITE)
#   paddle = pygame.draw.rect(window, GREEN,(paddle_x, paddle_y, paddle_width, paddle_height))
#   ball=pygame.draw.circle(window,BLACK,(ball_x,ball_y),ball_radius)
#   score_text=font.render("Score: "+str(Score),True,BLACK)
#   window.blit(score_text,(10,10))

#   pygame.display.update()

#   if ball.left<=0 or ball.right>=window_width:
#     ball_speed_x*=-1
#   if ball.top<=0:
#     ball_speed_y*=-1


#   if pygame.Rect.colliderect(ball,paddle):
#     ball_speed_y*=-1
#     Score+=-1
#   if ball.bottom>=window_height:
#     game_over=True


#   pygame.time.delay(30)

# window.fill(WHITE)
# score_text=font.render("Score: "+str(Score),True,BLACK)
# window.blit(score_text,(10,10))
# game_over_text=font.render("Game Over",True,BLACK)
# window.blit(game_over_text, ((window_width - game_over_text.get_width()) // 2, (window_height- game_over_text.get_height())//2))
# pygame.display.update()


# pygame.time.delay(2000)
# pygame.quit()
# sys.exit()





















# try:
#   import pygame
#   import sys
#   import math
#   from pygame.locals import QUIT, MOUSEBUTTONDOWN

#   pygame.init()

#   window_weight,window_height=600,400
#   window=pygame.display.set_mode((window_weight,window_height))
#   pygame.display.set_caption("Fidget Spinner")

#   WHITE=(255,255,255)
#   BLACK=(0,0,0)

#   background_image=pygame.image.load("background.jpeg").convert()
#   background_image=pygame.transform.scale(background_image,window_weight,window_height)

#   spinner_images=[
#     pygame.image.load("background1.jpeg").convert_alpha(),
#     pygame.image.load("background2.jpeg").convert_alpha(),
#     pygame.image.load("background3.jpeg").convert_alpha(),
#   ]

#   spinner_width,spinner_height=300,300
#   spinner_images=[pygame.transfrom.scale(image,(spinner_width,spinner_height)) for image in spinner_images]

#   spinner_x,spinner_y=window_weight//2,window_height//2
#   spinner_rotation=0

#   spinner_rotation_speed=0
#   current_spinner=0

#   font=pygame.font.Font(None,24)

#   def change_spinner():
#     global current_spinner
#     current_spinner+=1
#     if current_spinner>=len(spinner_images):
#       current_spinner=0

#   game_over=False

#   while not game_over:
#     for event in pygame.event.get():
#       if event.type==QUIT:
#         pygame.QUIT()
#         sys.exit()

#       if event.type==MOUSEBUTTONDOWN:
#         change_spinner()

#     mouse_x,mouse_y=pygame.mouse.get_pos()
#     angle=math.atan2(mouse_y-spinner_y,mouse_x-spinner_x)
#     spinner_rotation_speed=math.degrees(angle)

#     spinner_rotation+=spinner_rotation_speed
#     rotated_spinner=pygame.transform.rotate(spinner_images[current_spinner],-spinner_rotation)
#     spinner_rect=rotated_spinner.get_rect(center=(spinner_x,spinner_y))

#     window.blit(background_image,(0,0))
#     window.blit(rotated_spinner,spinner_rect)
#     pygame.display.update()
#     pygame.time.delay(30)


#   pygame.quit()
#   sys.exit()

# except Exception:
#   print("")
