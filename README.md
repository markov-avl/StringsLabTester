# StringsLabTester

## Установка

1. Устанавливаем Python 3 или выше
2. Компилируем свою программу так, чтобы `main` был эквивалентен:

```c++
#include <iostream>
#include "strings.h"

int main(int argc, char* argv[]) {
    std::cout << replace(String(argv[1]), String(argv[2]), String(argv[3]));
    return 0;
}
```

3. Кладем `main.exe` в директорию с `main.py`
4. Запускаем скрипт `main.py` из этой же директории
5. Смотрим ошибки


## Работа программы 

```yaml
Python result: " ktfcventmxbdqhegdawwuappeeriievdguvmzcesdrcegdnzihicmnlhpnrtmebrumowpa atiqrke"
C++ result: " ktfcventmxbdqhegdawwuappeeriievdguvmzces#drcegdnzihicmnlhpnrtmebrumowpa atiqrke"
Exception: Results don't match
Source string: " ktfcventmxbdqhegdawwuappeeriievdguvmzceshj"
To replace: "hj"
With replace: "drcegdnzihicmnlhpnrtmebrumowpa atiqrke"
Failed tests: 1
Successful tests: 472

Python result: "amfydjrurkm onntwxngoadgsglptxtuydfb sdpf  vwexgykkad"
C++ result: "amfydjrurkm onntwxngoadgsglptxtuydfb# sdpf  vwexgykkad"
Exception: Results don't match
Source string: "amfrja onntwxngoadgsglptxtuydfb sdpf  vwexgykkad"
To replace: "rja"
With replace: "ydjrurkm"
Failed tests: 2
Successful tests: 1067
```