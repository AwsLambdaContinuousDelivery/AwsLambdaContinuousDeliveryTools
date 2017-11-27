
from awacs.aws import Statement, Allow, Principal
from awacs.sts import AssumeRole
from awslambdacontinuousdelivery.tools import alphanum
from troposphere import Sub
from troposphere.iam import Role, Policy
from typing import List

import awacs.aws
import awacs.awslambda
import awacs.autoscaling
import awacs.codebuild
import awacs.codecommit
import awacs.codedeploy
import awacs.cloudformation
import awacs.cloudwatch
import awacs.iam
import awacs.ecs
import awacs.elasticbeanstalk
import awacs.elasticloadbalancing
import awacs.opsworks
import awacs.s3
import awacs.sns
import awacs.sqs
import awacs.rds

def defaultAssumeRolePolicyDocument(service: str) -> Policy:
  statement = Statement( Action = [AssumeRole]
                       , Effect = Allow
                       , Principal = Principal("Service", service)
                       )
  return awacs.aws.Policy( Statement = [ statement ] )

def createRole(name: str, policies: List[Policy]) -> Role:
  return Role( alphanum(name)
             , RoleName = Sub(name+"-${AWS::StackName}")
             , AssumeRolePolicyDocument = self._assumePolicy
             , Policies = policies
             )


def oneClickCodePipeServicePolicy() -> Policy:
  statements = [
      awacs.aws.Statement(
          Action = [ awacs.s3.GetObject
                   , awacs.s3.GetObjectVersion
                   , awacs.s3.GetBucketVersioning
                   ]
        , Resource = [ "*" ]
        , Effect = awacs.aws.Allow
        )
    , awacs.aws.Statement(
          Action = [ awacs.s3.PutObject ]
        , Resource = [ "arn:aws:s3:::codepipeline*" 
                     , "arn:aws:s3:::elasticbeanstalk*"
                     ]
        , Effect = awacs.aws.Allow
        )
    , awacs.aws.Statement(
          Action = [ awacs.codecommit.CancelUploadArchive
                   , awacs.codecommit.GetBranch
                   , awacs.codecommit.GetCommit
                   , awacs.codecommit.GetUploadArchiveStatus
                   , awacs.codecommit.UploadArchive
                   ]
        , Resource = [ "*" ]
        , Effect = awacs.aws.Allow
        )
    , awacs.aws.Statement(
        Action = [ awacs.codedeploy.CreateDeployment
                 , awacs.codedeploy.GetApplicationRevision
                 , awacs.codedeploy.GetDeployment
                 , awacs.codedeploy.GetDeploymentConfig
                 , awacs.codedeploy.RegisterApplicationRevision
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    , awacs.aws.Statement(
        Action = [ awacs.elasticbeanstalk.Action("*")
                 , awacs.ec2.Action("*")
                 , awacs.elasticloadbalancing.Action("*")
                 , awacs.autoscaling.Action("*")
                 , awacs.cloudwatch.Action("*")
                 , awacs.s3.Action("*")
                 , awacs.sns.Action("*")
                 , awacs.cloudformation.Action("*")
                 , awacs.rds.Action("*")
                 , awacs.sqs.Action("*")
                 , awacs.ecs.Action("*")
                 , awacs.iam.PassRole
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    , awacs.aws.Statement(
        Action = [ awacs.awslambda.InvokeFunction
                 , awacs.awslambda.ListFunctions
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    , awacs.aws.Statement(
        Action = [ awacs.opsworks.CreateDeployment
                 , awacs.opsworks.DescribeApps
                 , awacs.opsworks.DescribeCommands
                 , awacs.opsworks.DescribeDeployments
                 , awacs.opsworks.DescribeInstances
                 , awacs.opsworks.DescribeStacks
                 , awacs.opsworks.UpdateApp
                 , awacs.opsworks.UpdateStack
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    , awacs.aws.Statement(
        Action = [ awacs.cloudformation.CreateStack
                 , awacs.cloudformation.DeleteStack
                 , awacs.cloudformation.DescribeStacks
                 , awacs.cloudformation.UpdateStack
                 , awacs.cloudformation.CreateChangeSet
                 , awacs.cloudformation.DeleteChangeSet
                 , awacs.cloudformation.DescribeChangeSet
                 , awacs.cloudformation.ExecuteChangeSet
                 , awacs.cloudformation.SetStackPolicy
                 , awacs.cloudformation.ValidateTemplate
                 , awacs.iam.PassRole
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    , awacs.aws.Statement(
        Action = [ awacs.codebuild.BatchGetBuilds
                 , awacs.codebuild.StartBuild
                 ]
      , Resource = [ "*" ]
      , Effect = awacs.aws.Allow
      )
    ]
  policyDoc = awacs.aws.Policy( Statement = statements )
  return Policy(
        PolicyName = Sub("oneClickCodePipeServicePolicy-${AWS::StackName}")
      , PolicyDocument = policyDoc
      )