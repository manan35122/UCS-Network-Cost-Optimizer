# Cost-Efficient Data Packet Routing

## Project Overview

In a computer network, data packets must be transmitted efficiently from a source server to a destination server. Each link between routers has a different transmission cost, influenced by factors such as bandwidth, latency, congestion, and link quality. This project aims to determine the most cost-efficient route for a data packet to travel from the source router (Router A) to the destination router (Router F) using the **Uniform Cost Search (UCS)** algorithm.

## Problem Setup

The network is modeled as a graph where:

- **Nodes** represent routers in the network.
- **Edges** represent network links with associated transmission costs. These costs reflect real-world constraints.

### Network Graph

The following table illustrates the routers and their transmission costs:

| Router 1 | Router 2 | Transmission Cost |
|----------|----------|-------------------|
| A        | B        | 4                 |
| A        | C        | 2                 |
| B        | D        | 3                 |
| C        | D        | 1                 |
| C        | E        | 7                 |
| D        | F        | 5                 |
| E        | F        | 3                 |

## Task

The objective is to find the least costly path for the data packet to travel from the source server (Router A) to the destination server (Router F) using the UCS algorithm.

### Example Output

Using UCS, the algorithm explores various paths, such as:

- **Path:** A → C → D → F 
  - **Total Cost:** 2 + 1 + 5 = **8**
  
- **Path:** A → B → D → F 
  - **Total Cost:** 4 + 3 + 5 = **12**


