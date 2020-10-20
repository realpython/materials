#ifdef _MSC_VER
    #define EXPORT_SYMBOL __declspec(dllexport)
#else
    #define EXPORT_SYMBOL
#endif

EXPORT_SYMBOL float cmult(int int_param, float float_param);