from actors import SmallAnimal, Creature, Dragon, Wizard

nums = [1, 1, 2, 3, 5, 8, 13, 21]

for i, num in enumerate(nums):
    print(f'{i+1} {num}')

creatures = [SmallAnimal('Toad', 1),
            Creature('Tiger', 12),
            SmallAnimal('Bat', 3),
            Dragon('Dragon', 50, 75, True),
            Wizard('Evil Wizard', 1000)]

hero = Wizard('Gandolf', 75)

print('Hero battles: {}'.format(hero.attack(creatures[0])))