import { People } from "./people.js";
import { DebugForm } from "./debug.js";

function main() {
  new People();
  const debug = new DebugForm();
  debug.showResponse("");
}

main();
