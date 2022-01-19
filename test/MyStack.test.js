import { Template } from "aws-cdk-lib/assertions";
import * as sst from "@serverless-stack/resources";
import MyStack from "../stacks/MyStack";

test("Test Stack", () => {
  const app = new sst.App();
  app.setDefaultFunctionProps({
    runtime: "python3.7"
  });
  // WHEN
  const stack = new MyStack(app, "test-stack");
  // THEN
  const template = Template.fromStack(stack);
  template.resourceCountIs("AWS::Lambda::Function", 1);
});
