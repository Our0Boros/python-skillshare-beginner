### 13/04/2020
### Author: Omer Goder
### Using the pop method
### Using the remove method

subscribers = ['devilset91@gmail.com','omer.goder.docs@gmail.com','g.d.y.eng@gmail.com']

# Print the list
print(subscribers)
print("\n")

# Using the pop method - pop off the last(default) item of the list
# This will remove the item and store it in the new variable
popped_subscribers = subscribers.pop()

print(subscribers)

# Print the popped value
print(popped_subscribers)
print("\n")

# Reset the list
subscribers = ['devilset91@gmail.com','omer.goder.docs@gmail.com','g.d.y.eng@gmail.com']

# Using the pop method to pop the (0) item on the list
first_subscriber = subscribers.pop(0)

print(subscribers)

# Print the popped value
print(first_subscriber)
print("\n")

print("Your first subscriber was \'" + first_subscriber + "\'.\n")

subscribers = ['devilset91@gmail.com','omer.goder.docs@gmail.com','g.d.y.eng@gmail.com']

print(subscribers)

# Using the remove method - .remove('str')
subscribers.remove('omer.goder.docs@gmail.com')

print(subscribers)
print("\n")

subscribers = ['devilset91@gmail.com','omer.goder.docs@gmail.com','g.d.y.eng@gmail.com']

subscribed_by_mistake = 'omer.goder.docs@gmail.com'

subscribers.remove(subscribed_by_mistake)

print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up\n")