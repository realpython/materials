document.addEventListener("DOMContentLoaded", async () => {

    const allowUnicode = document.querySelector("#allow_unicode")
    const canonical = document.querySelector("#canonical")
    const content = document.querySelector("#content")
    const defaultFlowStyle = document.querySelector("#default_flow_style")
    const defaultStyle = document.querySelector("#default_style")
    const encoding = document.querySelector("#encoding")
    const explicitEnd = document.querySelector("#explicit_end")
    const explicitStart = document.querySelector("#explicit_start")
    const form = document.querySelector("form")
    const indent = document.querySelector("#indent")
    const lineBreak = document.querySelector("#line_break")
    const sortKeys = document.querySelector("#sort_keys")
    const version = document.querySelector("#version")
    const width = document.querySelector("#width")

    const getPayload = () => {
        return {

            // Boolean flags:
            allow_unicode: allowUnicode.checked,
            canonical: canonical.checked,
            default_flow_style: defaultFlowStyle.checked,
            explicit_end: explicitEnd.checked,
            explicit_start: explicitStart.checked,
            sort_keys: sortKeys.checked,

            // Valued parameters:
            indent: parseInt(indent.value),
            width: parseInt(width.value),
            default_style: defaultStyle.value,
            encoding: encoding.value || null,
            line_break: lineBreak.value,
            version: (version.value && version.value.split(".").map(x => parseInt(x))) || null,
        }
    }

    const reformat = async () => {
        try {
            const response = await fetch("/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(getPayload()),
            })
            content.value = await response.json()
        } catch (error) {
            alert(`Error: ${error}`)
        }
    }

    function showRangeValue() {
        this.previousElementSibling.innerText = this.value
    }

    form.addEventListener("change", reformat)
    indent.addEventListener("change", showRangeValue)
    width.addEventListener("change", showRangeValue)

    showRangeValue.call(indent)
    showRangeValue.call(width)
    await reformat()
})
