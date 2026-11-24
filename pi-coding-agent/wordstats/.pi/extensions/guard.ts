import {
  type ExtensionAPI,
  isToolCallEventType,
} from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  // Block shell commands that contain the word rm.
  pi.on("tool_call", async (event) => {
    if (
      isToolCallEventType("bash", event) &&
      /\brm\b/.test(event.input.command)
    ) {
      return { block: true, reason: "rm is blocked in this project" };
    }
  });

  // A custom tool the model can call.
  pi.registerTool({
    name: "count_lines",
    label: "Count lines",
    description: "Count the lines in a text file",
    parameters: Type.Object({ path: Type.String() }),
    async execute(_id, params) {
      const { readFileSync } = await import("node:fs");
      const n = readFileSync(params.path, "utf8").split("\n").length - 1;
      return { content: [{ type: "text", text: `${n} lines` }], details: {} };
    },
  });
}
