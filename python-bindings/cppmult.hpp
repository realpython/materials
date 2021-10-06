#ifdef _MSC_VER
    #define EXPORT_SYMBOL __declspec(dllexport)
#else
    #define EXPORT_SYMBOL
#endif

#ifdef __cplusplus
extern "C" {
#endif

EXPORT_SYMBOL float cppmult(int int_param, float float_param);

#ifdef __cplusplus
}
#endif
