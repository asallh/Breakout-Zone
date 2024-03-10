import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu";

export default function NavBar() {
  return (
    <div className="w-screen px-8">
      <div
        className="flex justify-between w-full p-4 px-8 border border-white rounded-xl"
      >
        {/* Replace this with image when i get that chance to make a logo */}
        <h1 className="flex items-center justify-start text-small font-bauer">
          Breakout Zone
        </h1>
        <div className="flex items-center">
          <DropdownMenu>
            <DropdownMenuTrigger>Select Versus</DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuLabel>Players</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem>1 v 1</DropdownMenuItem>
              <DropdownMenuItem>Single Player</DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuLabel>Team</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem>Team v Team</DropdownMenuItem>
              <DropdownMenuItem>Single Team</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </div>
  );
}
