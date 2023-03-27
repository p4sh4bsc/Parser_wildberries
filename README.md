# Парсер карточек товаров с Ozon

<table>
<thead>
<tr>
<th>Стат</th>
<th>Description</th>
<th>Color Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Working</td>
<td>Функция работает.</td>
<td><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/3e57f06b629286e78eb3dd0c6ba2bb34934fc7b3995b9692253e85552351a34c/68747470733a2f2f692e6962622e636f2f33466e745231632f312e706e67"><img src="https://camo.githubusercontent.com/3e57f06b629286e78eb3dd0c6ba2bb34934fc7b3995b9692253e85552351a34c/68747470733a2f2f692e6962622e636f2f33466e745231632f312e706e67" alt="Working" data-canonical-src="https://i.ibb.co/3FntR1c/1.png" style="max-width: 100%;"></a></td>
</tr>
<tr>
<td>Not Working</td>
<td>Функция не работает.</td>
<td><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67"><img src="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67" alt="Not-Working" data-canonical-src="https://i.ibb.co/wWtD8S6/2.png" style="max-width: 100%;"></a></td>
</tr>
</tbody>
</table>


## Фунционал:
1. Сбор ID, Названия товара, Цены товара, количества отзывов и время доставки.
2. Запись собранных данных в csv таблицу.
3. Сортировка по ценам и количеству отзывов.
4. Создание нового csv файла, если его размер достигает определенного значения.

## Документация:
#### -h, --help            show this help message and exit
#### -p [PRICE], --price [PRICE] Сортировка по убыванию цен
#### -s [STARS], --stars [STARS] Сортировка по убыванию отзывов

![Сни1111мок](https://user-images.githubusercontent.com/120973158/227800933-21e94c7d-e37a-4966-9f18-714336c8c3d8.PNG)

## Future:

<table>
<thead>
<tr>
<th>Sr.No.</th>
<th>Name</th>
<th>Description</th>
<th>Status</th>
</tr>
</thead>

<tbody>

<tr>
<td>1.</td>
<td>Запуск скрипта по времени.</td>
<td>Запуск повторного парсинга через определненное количество часов.</td>
<td><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/3e57f06b629286e78eb3dd0c6ba2bb34934fc7b3995b9692253e85552351a34c/68747470733a2f2f692e6962622e636f2f33466e745231632f312e706e67"><img src="https://camo.githubusercontent.com/3e57f06b629286e78eb3dd0c6ba2bb34934fc7b3995b9692253e85552351a34c/68747470733a2f2f692e6962622e636f2f33466e745231632f312e706e67" alt="Working" data-canonical-src="https://i.ibb.co/3FntR1c/1.png" style="max-width: 100%;"></a></td>
</tr>


<tr>
<td>2.</td>
<td>Написание асинхронного парсера.</td>
<td>Парсинг нескольких страниц одновременно.</td>
<td><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67"><img src="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67" alt="Not-Working" data-canonical-src="https://i.ibb.co/wWtD8S6/2.png" style="max-width: 100%;"></a></td>
</tr>

<tr>
<td>3.</td>
<td>Написание асинхронного парсера.</td>
<td>Парсинг нескольких страниц одновременно.</td>
<td><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67"><img src="https://camo.githubusercontent.com/bb9ddd4cbb612a1892a069fcddbdb3c43b17a9c1527a2c799d8f1dee722b7410/68747470733a2f2f692e6962622e636f2f775774443853362f322e706e67" alt="Not-Working" data-canonical-src="https://i.ibb.co/wWtD8S6/2.png" style="max-width: 100%;"></a></td>
</tr>

</tbody>
</table>







1. Написание асинхронного парсера. ❌

~~2. Запуск скрипта по времени.~~ ✅

3. Написание GUI ❌
