# GUI powered by UIFlow
## Manual / Руководство

### [English]
One day we met the UI in the Arduino IDE. Today, the trend of the company M5Stack is UIFlow, so from Arduino IDE had to move away, and as a consequence, and abandon all written facilities. In this lesson we will start to get acquainted with a new analog UI - GUI. The GUI will be written in the MicroPython programming language.

The graphical user interface contains elements such as: menus, buttons, icons, lists, progress and status bars, sliders and more; All of them are presented to the user on the display, executed usually in the form of graphical images.

In the GUI, the user has arbitrary access (using the standard three buttons: A, B, C; located on the front panel of the device) to all visible and focused screen elements and directly manipulates them.

Let's look at the structure of the GUI. Let's look at figure 1.

![](https://pp.userapi.com/c855520/v855520118/193bd/-fvJ3oivU1k.jpg)

Figure 1

The base unit is the GUIObject class, which has fields such as unique name, coordinates, dimensions, scene number, state, and others. GUIObject requires an external Live function that describes the behavior of the graphic element itself. When you create a new graphic element, you must create a Live function for it, using the standard set of available fields of the GUIObject class.

Okay, now let's look at figure 2. All graphic elements have a Scene field, which determines on which conditional scene this element will be present. All elements from all scenes are stored in the GUIRoll array (numbering starts from zero). As You have already understood, each element must have a unique name, which is located in the Name field. The active scene is the one whose number is specified in the global variable GUIActiveScene. You can change the number of the active scene only by using the GUIScene(Number) function, where Number is the number of the desired scene. 

![](https://pp.userapi.com/c855520/v855520118/193c6/BSdtZcTwqg0.jpg)

Figure 2

GUI is protected from the imposition of one graphic element to another. If the coordinates specified by the user will cause a conflict of free location, the element will automatically be assigned to the next new coordinates in the free space. Note that not all elements can be resized to Width and Height, but they can always return to their current dimensions.

![](https://pp.userapi.com/c855520/v855520118/193cf/T2vhPw-JOoI.jpg)

Figure 3

The Status (default 0) field is integral to any of the graphical elements. This field defines one of three States (as of today): 


0 - Visible (item is available and displayed);

1 - Touchable (item available, displayed, available for interaction); 

2 - Controllable (the element is entirely under user control, other elements are not available at the moment).

![](https://pp.userapi.com/c855520/v855520118/193d8/cJBv4TxX6QY.jpg)

Figure 4

The Focused field (default False) allows the element to take focus in the chain of scene elements. If the value is False, the item will ignore Status 1 and 2. This field is usually used for items that are used only to display information, but there are exceptions (figure 5).

![](https://pp.userapi.com/c855520/v855520118/193e1/ZZXlcYAv4yY.jpg)

Figure 5

If You plan to add animation, use the Time field. For example, GUIInputbox uses this field to blink the cursor (figure 6).

![](https://pp.userapi.com/c855520/v855520118/193ea/jTUaFQB1iKE.jpg)

Figure 6

Each graphic element has two data fields: TextValue for storing text data and NumberValue for storing numeric data. You can store different data at the same time, even if Your item doesn't use it. There is a related Label field used to store the displayed title of the element (figure 7). 

![](https://pp.userapi.com/c855520/v855520118/193f3/oMkZr1RKG2Y.jpg)

Figure 7

Each graphic element has an optional Function (default None) field that stores a pointer to a custom function. Imagine that You want to make a button that changes the value of the text field of the graphic element named "human1". Create a function and associate it with the Function field of Your element (figure 8). Note that the user-defined function must take as an argument a pointer to an instance of the GUIObject class that called the function itself.

![](https://pp.userapi.com/c855520/v855520118/193fc/2txpXC4RGvI.jpg)

Figure 8

Okay, now, for example, let's try to create a button on scene number 0:

	obj = GUIObject()
	obj.Name = "myFirstButton"
	obj.Type = "button"
	obj.Label = "My button"
	obj.X = 10
	obj.Y = 19
	obj.Scene = 0
	obj.Focusable = True
	GUIAttach(obj)
	obj = None

### [По-русски]
Однажды мы познакомились с UI в Arduino IDE. Сегодня трендом компании M5Stack явлется UIFlow, поэтому от Arduino IDE пришлось отойти, а как следствие и отказаться от всех написанных удобств. В этом уроке мы начнём знакомиться с новым аналогом UI - GUI. GUI будет написан на языке программирования MicroPython.

Графический интерфейс пользователя содержит элементы, такие как: меню, кнопки, значки, списки, прогресс и статус бары, ползунки и многое другое; Все они представлены пользователю на дисплее, исполнены, как правило, в виде графических изображений.

В GUI пользователь имеет произвольный доступ (с помощью стандартных трёх кнопок: A, B, C; расположенных на лицевой панели устройства) ко всем видимым и фокусируемым экранным элементам и осуществляет непосредственное манипулирование ими.

Давайте познакомимся со структурой GUI. Давайте посмотрим на рисунок 1.

![](https://pp.userapi.com/c855520/v855520118/193bd/-fvJ3oivU1k.jpg)

Рисунок 1

Базовой единицей является класс GUIObject, который имеет поля, такие как уникальное имя, координаты, размеры, номер сцены, состояние и другие. GUIObject требует внешнюю Live-функцию, которая описывает характер поведения непосредственно самого графического элемента. При создании нового графического элемента необходимо создавать для него Live-функцию, при этом использовать стандартный набор доступных полей класса GUIObject.

Хорошо, теперь давайте посмотрим на рисунок 2. Все графические элементы имеют поле Scene, которое определяет на какой условной сцене будет присутствовать данный элемент. Все элементы со всех сцен хранятся в массиве GUIRoll (нумерация начинается с нуля). Как Вы уже поняли, каждый элемент обязательно должен иметь уникальное имя, которое располагается в поле Name. Активной сценой является та, чей номер указан в глобальной переменной GUIActiveScene. Изменять номер активной сцены разрешено  исключительно с помощью функции GUIScene(Number), где Number - есть номер желаемой сцены. 

![](https://pp.userapi.com/c855520/v855520118/193c6/BSdtZcTwqg0.jpg)

Рисунок 2

GUI имеет защиту от наложения одного графического элемента на другой. Если координаты указанные пользователем будет вызывать противоречия свободного расположения, то элементу автоматически будут присвоены новые ближайшие координаты в свободном месте. Обратите внимание на то, что не все элементы поддаются изменению размеров Width и Height, но при этом всегда могут возвращать свои текущие размеры.

![](https://pp.userapi.com/c855520/v855520118/193cf/T2vhPw-JOoI.jpg)

Рисунок 3

Поле Status (default 0) является неотъемлемым для любого из графических элементов. Данное поле определяет одно из трёх состояний (на сегодняшний день): 


0 - Visible (элемент доступен и отображается);
1 - Touchable (элемент доступен, отображается, доступен для взаимодействия); 
2 - Controllable (элемент находится целиком под управлением пользователя, другие элементы недоступны в данный момент).

![](https://pp.userapi.com/c855520/v855520118/193d8/cJBv4TxX6QY.jpg)

Рисунок 4

Поле Focusable (default False) позволяет элементу принимать на себя фокус в цепи элементов сцены. Если значение оставить False, то элемент будет игнорировать Status 1 и 2. Данное поле используют, как правило, для элементов, которые применяются только для отображения информации, но бывают исключения (рисунок 5).

![](https://pp.userapi.com/c855520/v855520118/193e1/ZZXlcYAv4yY.jpg)

Рисунок 5

Если Вы планируете добавить анимацию, то используйте поле Time. Например GUIInputbox использует данное поле для мигания курсором (рисунок 6).

![](https://pp.userapi.com/c855520/v855520118/193ea/jTUaFQB1iKE.jpg)

Рисунок 6

Каждый графический элемент имеет два поля данных: TextValue для хранения текстовых данных и NumberValue для хранения числовых данных. Вы можете хранить одновременно разные данные, даже если Ваш элемент не будет использовать их. Есть родственное поле Label, используется для хранения отображаемого заголовка элемента (рисунок 7). 

![](https://pp.userapi.com/c855520/v855520118/193f3/oMkZr1RKG2Y.jpg)

Рисунок 7

Каждый графический элемент имеет необязательное поле Function (default None), которое хранит указатель на пользовательскую функцию. Представьте себе, что Вы хотите сделать кнопку при нажатии на которую изменяется значение текстового поля графического элемента с именем "human1". Создайте функцию и свяжите её с полем  Function Вашего элемента (рисунок 8). Обратите внимание на то, что пользовательская функция должна принимать в качестве аргумента указатель на экземпляр класса GUIObject вызвавшего саму функцию.

![](https://pp.userapi.com/c855520/v855520118/193fc/2txpXC4RGvI.jpg)

Рисунок 8

Хорошо, теперь, для примера, давайте попробуем создать кнопку на сцене под номером 0:

	obj = GUIObject()
	obj.Name = "myFirstButton"
	obj.Type = "button"
	obj.Label = "My button"
	obj.X = 10
	obj.Y = 19
	obj.Scene = 0
	obj.Focusable = True
	GUIAttach(obj)
	obj = None