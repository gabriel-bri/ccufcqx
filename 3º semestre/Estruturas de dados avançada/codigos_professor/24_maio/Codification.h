#ifndef D511CC0E_D851_478E_94C9_545213265EAA
#define D511CC0E_D851_478E_94C9_545213265EAA
#include <string>

size_t code_std_string(const std::string& str) {
    size_t code = 0, BASE = 127;
    for(size_t i = 0; str[i] != '\0'; ++i) {
        code = (code * BASE) + str[i];
    }
    return code;
}

size_t code_string(const char* str, size_t len) {
    size_t code = 0, BASE = 127;
    for(size_t i = 0; i < len; ++i) {
        code = (code * BASE) + str[i];
    }
    return code;
}

size_t code_int(const int& value) {
    size_t len = sizeof(value);
    const char *x = reinterpret_cast<const char*>(&value);
    return code_string(x, len);
}

size_t code_float(const float& value) {
    size_t len = sizeof(value);
    const char *x = reinterpret_cast<const char*>(&value);
    return code_string(x, len);
}

#endif /* D511CC0E_D851_478E_94C9_545213265EAA */
