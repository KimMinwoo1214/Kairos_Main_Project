# flake8: noqa

# auto-generated DO NOT EDIT

from rcl_interfaces.msg import ParameterDescriptor
from rcl_interfaces.msg import SetParametersResult
from rcl_interfaces.msg import FloatingPointRange, IntegerRange
from rclpy.clock import Clock
from rclpy.exceptions import InvalidParameterValueException
from rclpy.time import Time
import copy
import rclpy
import rclpy.parameter
from generate_parameter_library_py.python_validators import ParameterValidators



class tree_node_parameters:

    class Params:
        # for detecting if the parameter struct has been updated
        stamp_ = Time()

        node_modules = ["ros_bt_py.nodes", "ros_bt_py.ros_nodes"]
        tree_storage_paths = ["$HOME/.ros"]
        show_traceback_on_exception = False
        diagnostics_frequency_hz = 1.0
        class __DefaultTree:
            load_default_tree = False
            load_default_tree_permissive = False
            tick_frequency_hz = 10.0
            tree_path = ""
            control_command = 2
        default_tree = __DefaultTree()



    class ParamListener:
        def __init__(self, node, prefix=""):
            self.prefix_ = prefix
            self.params_ = tree_node_parameters.Params()
            self.node_ = node
            self.logger_ = rclpy.logging.get_logger("tree_node_parameters." + prefix)

            self.declare_params()

            self.node_.add_on_set_parameters_callback(self.update)
            self.clock_ = Clock()

        def get_params(self):
            tmp = self.params_.stamp_
            self.params_.stamp_ = None
            paramCopy = copy.deepcopy(self.params_)
            paramCopy.stamp_ = tmp
            self.params_.stamp_ = tmp
            return paramCopy

        def is_old(self, other_param):
            return self.params_.stamp_ != other_param.stamp_

        def unpack_parameter_dict(self, namespace: str, parameter_dict: dict):
            """
            Flatten a parameter dictionary recursively.

            :param namespace: The namespace to prepend to the parameter names.
            :param parameter_dict: A dictionary of parameters keyed by the parameter names
            :return: A list of rclpy Parameter objects
            """
            parameters = []
            for param_name, param_value in parameter_dict.items():
                full_param_name = namespace + param_name
                # Unroll nested parameters
                if isinstance(param_value, dict):
                    nested_params = self.unpack_parameter_dict(
                            namespace=full_param_name + rclpy.parameter.PARAMETER_SEPARATOR_STRING,
                            parameter_dict=param_value)
                    parameters.extend(nested_params)
                else:
                    parameters.append(rclpy.parameter.Parameter(full_param_name, value=param_value))
            return parameters

        def set_params_from_dict(self, param_dict):
            params_to_set = self.unpack_parameter_dict('', param_dict)
            self.update(params_to_set)

        def refresh_dynamic_parameters(self):
            updated_params = self.get_params()
            # TODO remove any destroyed dynamic parameters

            # declare any new dynamic parameters


        def update(self, parameters):
            updated_params = self.get_params()

            for param in parameters:
                if param.name == self.prefix_ + "node_modules":
                    validation_result = ParameterValidators.size_gt(param, 0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.node_modules = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "tree_storage_paths":
                    validation_result = ParameterValidators.size_gt(param, 0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.tree_storage_paths = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "show_traceback_on_exception":
                    updated_params.show_traceback_on_exception = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "diagnostics_frequency_hz":
                    validation_result = ParameterValidators.gt(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.diagnostics_frequency_hz = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "default_tree.load_default_tree":
                    updated_params.default_tree.load_default_tree = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "default_tree.load_default_tree_permissive":
                    updated_params.default_tree.load_default_tree_permissive = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "default_tree.tick_frequency_hz":
                    validation_result = ParameterValidators.gt(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.default_tree.tick_frequency_hz = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "default_tree.tree_path":
                    updated_params.default_tree.tree_path = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "default_tree.control_command":
                    validation_result = ParameterValidators.one_of(param, [0, 1, 2, 3, 4, 5, 6, 7])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.default_tree.control_command = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))



            updated_params.stamp_ = self.clock_.now()
            self.update_internal_params(updated_params)
            return SetParametersResult(successful=True)

        def update_internal_params(self, updated_params):
            self.params_ = updated_params

        def declare_params(self):
            updated_params = self.get_params()
            # declare all parameters and give default values to non-required ones
            if not self.node_.has_parameter(self.prefix_ + "node_modules"):
                descriptor = ParameterDescriptor(description="Python modules containing nodes to load on startup.", read_only = True)
                parameter = updated_params.node_modules
                self.node_.declare_parameter(self.prefix_ + "node_modules", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "tree_storage_paths"):
                descriptor = ParameterDescriptor(description="Paths where trees can be saved!.", read_only = True)
                parameter = updated_params.tree_storage_paths
                self.node_.declare_parameter(self.prefix_ + "tree_storage_paths", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "show_traceback_on_exception"):
                descriptor = ParameterDescriptor(description="Show error traceback on exception", read_only = True)
                parameter = updated_params.show_traceback_on_exception
                self.node_.declare_parameter(self.prefix_ + "show_traceback_on_exception", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "diagnostics_frequency_hz"):
                descriptor = ParameterDescriptor(description="Default frequency to publish diagnostics updates", read_only = True)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.diagnostics_frequency_hz
                self.node_.declare_parameter(self.prefix_ + "diagnostics_frequency_hz", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "default_tree.load_default_tree"):
                descriptor = ParameterDescriptor(description="Load default BT on startup", read_only = True)
                parameter = updated_params.default_tree.load_default_tree
                self.node_.declare_parameter(self.prefix_ + "default_tree.load_default_tree", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "default_tree.load_default_tree_permissive"):
                descriptor = ParameterDescriptor(description="Allow permissive loading of default BT", read_only = True)
                parameter = updated_params.default_tree.load_default_tree_permissive
                self.node_.declare_parameter(self.prefix_ + "default_tree.load_default_tree_permissive", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "default_tree.tick_frequency_hz"):
                descriptor = ParameterDescriptor(description="Tick frequency of the default BT", read_only = True)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.default_tree.tick_frequency_hz
                self.node_.declare_parameter(self.prefix_ + "default_tree.tick_frequency_hz", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "default_tree.tree_path"):
                descriptor = ParameterDescriptor(description="Path to the BT to load on startup!", read_only = True)
                parameter = updated_params.default_tree.tree_path
                self.node_.declare_parameter(self.prefix_ + "default_tree.tree_path", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "default_tree.control_command"):
                descriptor = ParameterDescriptor(description="Default command when running the default tree!", read_only = True)
                parameter = updated_params.default_tree.control_command
                self.node_.declare_parameter(self.prefix_ + "default_tree.control_command", parameter, descriptor)

            # TODO: need validation
            # get parameters and fill struct fields
            param = self.node_.get_parameter(self.prefix_ + "node_modules")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.size_gt(param, 0)
            if validation_result:
                raise InvalidParameterValueException('node_modules',param.value, 'Invalid value set during initialization for parameter node_modules: ' + validation_result)
            updated_params.node_modules = param.value
            param = self.node_.get_parameter(self.prefix_ + "tree_storage_paths")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.size_gt(param, 0)
            if validation_result:
                raise InvalidParameterValueException('tree_storage_paths',param.value, 'Invalid value set during initialization for parameter tree_storage_paths: ' + validation_result)
            updated_params.tree_storage_paths = param.value
            param = self.node_.get_parameter(self.prefix_ + "show_traceback_on_exception")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.show_traceback_on_exception = param.value
            param = self.node_.get_parameter(self.prefix_ + "diagnostics_frequency_hz")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('diagnostics_frequency_hz',param.value, 'Invalid value set during initialization for parameter diagnostics_frequency_hz: ' + validation_result)
            updated_params.diagnostics_frequency_hz = param.value
            param = self.node_.get_parameter(self.prefix_ + "default_tree.load_default_tree")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.default_tree.load_default_tree = param.value
            param = self.node_.get_parameter(self.prefix_ + "default_tree.load_default_tree_permissive")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.default_tree.load_default_tree_permissive = param.value
            param = self.node_.get_parameter(self.prefix_ + "default_tree.tick_frequency_hz")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('default_tree.tick_frequency_hz',param.value, 'Invalid value set during initialization for parameter default_tree.tick_frequency_hz: ' + validation_result)
            updated_params.default_tree.tick_frequency_hz = param.value
            param = self.node_.get_parameter(self.prefix_ + "default_tree.tree_path")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.default_tree.tree_path = param.value
            param = self.node_.get_parameter(self.prefix_ + "default_tree.control_command")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, [0, 1, 2, 3, 4, 5, 6, 7])
            if validation_result:
                raise InvalidParameterValueException('default_tree.control_command',param.value, 'Invalid value set during initialization for parameter default_tree.control_command: ' + validation_result)
            updated_params.default_tree.control_command = param.value


            self.update_internal_params(updated_params)
