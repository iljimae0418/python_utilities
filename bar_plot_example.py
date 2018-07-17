from matplotlib import pyplot as plt
movies = ["mov1","mov2","mov3","mov4","mov5"] 
num_oscars = [1,2,3,4,5] 
# bars are by default width 0.8, so we will add 0.1 to the left coordinates 
# so that each bar is centered 
xs = [i + 0.1 for i, _ in enumerate(movies)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel('# of Academy Awards')
plt.title("My Favorite Movies") 
# label x-axis with movie names at bar centers 
plt.xticks([i+0.5 for i, _ in enumerate(movies)],movies)

plt.show() 
