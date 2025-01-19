#!/bin/bash

kubectl run -i --tty --rm debug --image=busybox --restart=Never --namespace default -- /bin/sh

