# Gradient domain blending

The goal of this project was to seamlessly stitch an object from a "source" image to a "target" image. While a simple cut-and-paste method would bring the source onto the target, the result would be far from seamless. Instead, using Poisson blending, we attempted to preserve the gradient of the source match that of the target. Since humans are more sensitive to gradients than image intesities, this gradient domain blending looks more natural and less doctored than a naive cut-and-paste method.
