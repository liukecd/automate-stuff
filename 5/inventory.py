
# coding: utf-8

# # 好玩游戏的物品清单

# In[5]:

def dispalyInventory(inventory):
    total = 0
    print('Inventory:')
    for k, v in inventory.items():
        total += v
        print(v, k)
    print('Total number of items:', total)


# In[6]:

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dispalyInventory(stuff)

