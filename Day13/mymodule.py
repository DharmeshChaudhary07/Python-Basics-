def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

person2 = {
  "name": "sam",
  "age": 34,
  "country": "Aussie"
}

person3 = {
  "name": "Ramu",
  "age": 74,
  "country": "srilanka"
}


# # if __name__ == "__main__": is only useful when you want to write some quick tests inside your module file while building it, but don't want those tests to run when someone imports it.
# # Most beginners just ignore it and keep their module clean. As you grow and build bigger projects you'll naturally start using it. For now just remember:

# # module file → only define functions and variables, nothing else
# # main.py → write all your running code here

# # That's the clean way to do it! ✅

if __name__ == "__main__":
    greeting("Jonathan")  # ← just checking it works 
    print(person1)
    print("hello dumbo")