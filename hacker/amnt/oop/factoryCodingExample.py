from abc import ABC, abstractmethod

class Bullet(ABC):
    @abstractmethod
    def damage(self) -> int:
        pass

    @abstractmethod
    def velocity(self) -> int:
        pass

    @abstractmethod
    def health(self) -> int:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class Slow(Bullet):
    def damage(self) -> int:
        return 5

    def velocity(self) -> int:
        return 30

    def health(self) -> int:
        return 3

    def description(self) -> str:
        return "Slow bullet, high health"

class Fast(Bullet):
    def damage(self) -> int:
        return 10

    def velocity(self) -> int:
        return 100

    def health(self) -> int:
        return 1

    def description(self) -> str:
        return "Fast bullet, low health"

class Splash(Bullet):
    def damage(self) -> int:
        return 15*15

    def velocity(self) -> int:
        return 60

    def health(self) -> int:
        return 2

    def description(self) -> str:
        return "Explosive splash damage bullet"

class BulletFactory:
    def __init__(self, bullet_id: str):
        self.bullet_id = bullet_id

    def get_bullet(self) -> Bullet:
        match self.bullet_id:
            case "fast":
                return Fast()
            case "slow":
                return Slow()
            case "splash":
                return Splash()
            case _:
                raise ValueError(f"Unknown bullet type: {self.bullet_id}")

# Example usage
factory = BulletFactory("fast")
bullet = factory.get_bullet()
print(bullet.description())
