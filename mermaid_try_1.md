```mermaid

flowchart TD;
    
    setup_dev((Setup))
    style setup_dev fill:yellow    
        
    bci{{Build Container Image In Dev}}
    style bci fill:blue

    bci_Lima(Lima)
    bci_buildpacks(Cloud Native Buildpacks / CNB)


    setup_dev --> bci
    bci --> bci_Lima
    bci --> bci_buidpacks

```