def main():

    base_dmg = int(input('Enter base damage: ')) # base weapon damage
    weapon_dmg = int(input('Enter weapon damage: ')) # total of + weapon damage attribute
    physical_power = float(input('Enter physical power bonus: ')) # your physical power bonus % (enter as -+0.00)
    add_dmg = int(input('Enter additional damage: ')) # total of additional physical damage
    true_dmg = int(input('Enter true damage: ')) # total of additional true damage
    phys_reduction = float(input('Enter physical reduction: ')) # Put in phys reduc values you might fight against, or 0 for flat rate
    head = 1.50
    body = .50
    stat_dmg_head = ((((base_dmg + weapon_dmg) * (1+physical_power) + add_dmg) * head)+true_dmg)
    stat_dmg_body = ((((base_dmg + weapon_dmg) * (1+physical_power) + add_dmg) * body)+true_dmg)
    reduc_dmg = ((((base_dmg + weapon_dmg) * (1+physical_power) + add_dmg) * head) * (1-phys_reduction) + true_dmg)
    dummy_dmg = ((((base_dmg + weapon_dmg) * (1+physical_power) + add_dmg) * head) * (1+.22) + true_dmg)
    print(f'\ndamage to head: {stat_dmg_head:.2f}')
    print(f'damage to body: {stat_dmg_body:.2f}')
    print(f'headshot when phys reduction is {phys_reduction}: {reduc_dmg:.2f}')
    print(f'damage to dummy head in lobby: {dummy_dmg}')
main()