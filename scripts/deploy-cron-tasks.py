import sys

import boto3


class DeployCronTasks(object):
    boto_client = boto3.client('ecs')
    task_definition = None
    image_tag = None

    def __init__(self, task_definition, image_tag):
        self.task_definition = task_definition
        self.image_tag = image_tag

    def update_task_definition(self):
        print('==================================\n')
        print('= Start updating task definition =\n')
        print('==================================\n\n')
        task = self.boto_client.describe_task_definition(
            taskDefinition=self.task_definition
        )
        container_definitions = task.get('taskDefinition', {}).get('containerDefinitions')
        family = task.get('taskDefinition', {}).get('family')
        revision = task.get('taskDefinition', {}).get('revision')

        for item in container_definitions:
            image = item.get('image')
            new_image = '{}:{}'.format(image.split(':')[0], self.image_tag)
            item.update({'image': new_image})

        print('Registering new task definition - Revision {}\n'.format(revision + 1))
        self.boto_client.register_task_definition(
            family=family, containerDefinitions=container_definitions
        )

        print('Deregistering task definition - Revision {}\n'.format(revision))
        self.boto_client.deregister_task_definition(
            taskDefinition='{}:{}'.format(family, revision)
        )


if __name__ == "__main__":
    tag = sys.argv[1]
    task_definitions = sys.argv[2:]

    for tk in task_definitions:
        deploy_task = DeployCronTasks(task_definition=tk, image_tag=tag)

        # Update task
        deploy_task.update_task_definition()
