from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    os.makedirs('characters', exist_ok=True)

    card_count = int(input("Сколько карточек хотите добавить? "))
    for number in range(card_count):
        clases_base ={
            "Маг":{
                "strength":random.randint(1,3),
                "agility":random.randint(1,3),
                "intelligence":15,
                "luck":random.randint(1,3),
                "temper":random.randint(1,3),
                "skills":['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                "image":"images/wizard.png"
            },
            "Воин":{
                "strength":15,
                "agility":random.randint(1,3),
                "intelligence":random.randint(1,3),
                "luck":random.randint(1,3),
                "temper":random.randint(1,3),
                "skills":['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                "image":"images/warrior.png"
            },
            "Убийца":{
                "strength":random.randint(1,3),
                "agility":random.randint(1,3),
                "intelligence":random.randint(1,3),
                "luck":15,
                "temper":random.randint(1,3),
                "skills":['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                "image":"images/assasin.png"
            },
            "Бард":{
                "strength":random.randint(1,3),
                "agility":random.randint(1,3),
                "intelligence":random.randint(1,3),
                "luck":random.randint(1,3),
                "temper":15,
                "skills":['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                "image":"images/bard.webp"
            },
            "Охотник":{
                "strength":random.randint(1,3),
                "agility":15,
                "intelligence":random.randint(1,3),
                "luck":random.randint(1,3),
                "temper":random.randint(1,3),
                "skills": ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                "image":"images/archer.png"
            }   
        }
        character_classes = ["Охотник","Убийца","Маг","Воин","Бард"]
        character_races = ["гном","человек","эльф","оборотень"]
        character_name = input("Введите имя персонажа: ")
        character_race = int(input("Выберите рассу: 1-гном 2-человек 3-эльф 4-оборотень "))
        character_class = int(input("Выберите класс: 1-охотник 2-убийца 3-маг 4-воин 5-бард: "))
        skills = clases_base[character_classes[character_class-1]]["skills"]
        skills_sample = random.sample(skills,3)
        rendered_page = template.render(
            name=character_name,
            race=character_races[character_race-1],
            character_class=character_classes[character_class-1],
            strength=clases_base[character_classes[character_class-1]]["strength"],
            agility=clases_base[character_classes[character_class-1]]["agility"],
            intelligence=clases_base[character_classes[character_class-1]]["intelligence"],
            luck=clases_base[character_classes[character_class-1]]["luck"],
            temper=clases_base[character_classes[character_class-1]]["temper"],
            image=clases_base[character_classes[character_class-1]]["image"],
            first_skill = skills_sample[0],
            second_skill = skills_sample[1],
            third_skill = skills_sample[2],
        )

        with open(f'characters/index{number+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
 
            
if __name__ == '__main__':
    main()