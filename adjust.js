export default function adjustNodes(nodes) {
    const gridSize = Math.ceil(Math.sqrt(nodes.length)); // Determine grid size for square layout
    const nodeWidth = 50; // Minimum width for each node
    const nodeHeight = 50; // Height for each node
    const xOffset = 200; // Offset to create space between nodes
    const yOffset = 100; // Offset to create space between nodes
  
    return nodes.map((node, index) => {
      const row = Math.floor(index / gridSize);
      const col = index % gridSize;
  
      const width = node.name.length * 10 + nodeWidth; // Width based on character length with a base width
  
      return {
        ...node,
        position: {
          x: col * xOffset,
          y: row * yOffset,
        },
        style: {
          width: `${width}px`,
          height: `${nodeHeight}px`,
        }
      };
    });
  }
  
//   // Example usage with your provided data:
//   const data = {
//     "nodes": [
//       { "name": "User", "parentId": null, "type": "pool" },
//       { "name": "Login", "parentId": "User", "type": "start event" },
//       { "name": "Select Items", "parentId": "User", "type": "user task" },
//       { "name": "Set Payment Method", "parentId": "User", "type": "user task" },
//       { "name": "Select Reward", "parentId": "User", "type": "user task" },
//       { "name": "Pay", "parentId": "User", "type": "user task" },
//       { "name": "Complete Installment Agreement", "parentId": "User", "type": "user task" },
//       { "name": "Confirm Payment", "parentId": "User", "type": "user task" },
//       { "name": "Receive Items", "parentId": "User", "type": "user task" },
//       { "name": "Return Items", "parentId": "User", "type": "user task" },
//       { "name": "Exchange Items", "parentId": "User", "type": "user task" },
//       { "name": "System", "parentId": null, "type": "pool" },
//       { "name": "Prepare Items for Delivery", "parentId": "System", "type": "system task" },
//       { "name": "Resend Items", "parentId": "System", "type": "system task" },
//       { "name": "AND 1", "parentId": null, "type": "and gateway" },
//       { "name": "XOR 1", "parentId": null, "type": "xor gateway" },
//       { "name": "XOR 2", "parentId": null, "type": "xor gateway" },
//       { "name": "AND 2", "parentId": null, "type": "and gateway" },
//       { "name": "Delivery Complete", "parentId": null, "type": "end event" }
//     ],
//     "edges": [
//       { "from": "Login", "to": "Select Items" },
//       { "from": "Select Items", "to": "Set Payment Method" },
//       { "from": "Set Payment Method", "to": "AND 1" },
//       { "from": "AND 1", "to": "Select Reward" },
//       { "from": "Select Reward", "to": "XOR 1" },
//       { "from": "XOR 1", "to": "Pay", "condition": "Condition 1" },
//       { "from": "XOR 1", "to": "Complete Installment Agreement", "condition": "Condition 2" },
//       { "from": "Pay", "to": "Confirm Payment" },
//       { "from": "Complete Installment Agreement", "to": "Confirm Payment" },
//       { "from": "Confirm Payment", "to": "Prepare Items for Delivery" },
//       { "from": "Prepare Items for Delivery", "to": "Receive Items" },
//       { "from": "Receive Items", "to": "XOR 2" },
//       { "from": "XOR 2", "to": "Return Items", "condition": "Condition 3" },
//       { "from": "XOR 2", "to": "Exchange Items", "condition": "Condition 4" },
//       { "from": "Return Items", "to": "AND 2" },
//       { "from": "Exchange Items", "to": "AND 2" },
//       { "from": "AND 2", "to": "Resend Items" },
//       { "from": "Resend Items", "to": "Delivery Complete" }
//     ]
//   };
  
//   const adjustedNodes = adjustNodes(data.nodes);
//   console.log(adjustedNodes);
  