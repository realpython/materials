import { People } from "./people.js";
import { DebugForm } from "./debug.js";

function main() {
  new People();
  if (document.querySelector(".debug-card")) {
    const debug = new DebugForm();
    debug.showResponse("");
  }
}

main();
